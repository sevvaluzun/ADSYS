from django.db import models


class Campaign(models.Model):
    title = models.CharField("Kampanya Başlığı", max_length=200)
    location = models.CharField("Bölge", max_length=150)
    description = models.TextField("Açıklama")

    target_amount = models.DecimalField("Hedef Tutar", max_digits=12, decimal_places=2)
    collected_amount = models.DecimalField("Toplanan Tutar", max_digits=12, decimal_places=2, default=0)

    needs = models.TextField("İhtiyaç Listesi", blank=True)
    official_link = models.URLField("Resmi Bağış Linki", blank=True)

    image = models.ImageField(upload_to="campaigns/", blank=True, null=True)
    active = models.BooleanField("Aktif mi?", default=True)

    created_at = models.DateTimeField("Oluşturulma Tarihi", auto_now_add=True)

    class Meta:
        verbose_name = "Bağış Kampanyası"
        verbose_name_plural = "Bağış Kampanyaları"

    def progress_percent(self):
        if self.target_amount == 0:
            return 0
        return int((self.collected_amount / self.target_amount) * 100)

    def __str__(self):
        return self.title


class Volunteer(models.Model):
    SUPPORT_CHOICES = [
        ("saglik", "Sağlık"),
        ("lojistik", "Lojistik"),
        ("psikolojik", "Psikolojik Destek"),
        ("arama_kurtarma", "Arama Kurtarma"),
        ("diger", "Diğer"),
    ]

    full_name = models.CharField("Ad Soyad", max_length=150)
    phone = models.CharField("Telefon", max_length=30)
    email = models.EmailField("E-Posta")
    city = models.CharField("Şehir", max_length=100)

    support_area = models.CharField(
        "Destek Alanı",
        max_length=50,
        choices=SUPPORT_CHOICES
    )

    message = models.TextField("Açıklama", blank=True)
    created_at = models.DateTimeField("Başvuru Tarihi", auto_now_add=True)

    class Meta:
        verbose_name = "Gönüllü Başvurusu"
        verbose_name_plural = "Gönüllü Başvuruları"

    def __str__(self):
        return self.full_name


class PreparednessCheck(models.Model):
    user = models.OneToOneField(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="preparedness_check"
    )

    emergency_bag = models.BooleanField("Deprem çantam hazır", default=False)
    meeting_area = models.BooleanField("Toplanma alanını biliyorum", default=False)
    first_aid = models.BooleanField("İlk yardım çantam var", default=False)
    family_plan = models.BooleanField("Aile afet planım hazır", default=False)
    emergency_numbers = models.BooleanField("Acil telefonlar kayıtlı", default=False)
    powerbank = models.BooleanField("Powerbank dolu", default=False)
    flashlight = models.BooleanField("El fenerim hazır", default=False)
    water_food = models.BooleanField("Su ve dayanıklı gıda hazır", default=False)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Hazırlık Kontrolü"
        verbose_name_plural = "Hazırlık Kontrolleri"

    def progress_percent(self):
        fields = [
            self.emergency_bag,
            self.meeting_area,
            self.first_aid,
            self.family_plan,
            self.emergency_numbers,
            self.powerbank,
            self.flashlight,
            self.water_food,
        ]

        completed = sum(1 for field in fields if field)
        return int((completed / len(fields)) * 100)

    def __str__(self):
        return f"{self.user.username} hazırlık durumu"

class DonationCenter(models.Model):
    STATUS_CHOICES = [
        ("dusuk", "Düşük Yoğunluk"),
        ("orta", "Orta Yoğunluk"),
        ("kritik", "Kritik Yoğunluk"),
    ]

    campaign = models.ForeignKey(
        Campaign,
        on_delete=models.CASCADE,
        related_name="centers",
        verbose_name="Kampanya",
    )

    name = models.CharField("Merkez Adı", max_length=200)
    city = models.CharField("Şehir", max_length=100)
    address = models.TextField("Adres")

    capacity = models.PositiveIntegerField("Toplam Kapasite", default=100)
    current_load = models.PositiveIntegerField("Mevcut Doluluk", default=0)
    latitude = models.FloatField("Enlem", null=True, blank=True)
    longitude = models.FloatField("Boylam", null=True, blank=True)
    status = models.CharField(
        "Yoğunluk Durumu",
        max_length=20,
        choices=STATUS_CHOICES,
        default="dusuk"
    )

    manager = models.CharField("Merkez Sorumlusu", max_length=150, blank=True)
    phone = models.CharField("İletişim", max_length=30, blank=True)
    working_hours = models.CharField("Çalışma Saatleri", max_length=100, default="24 Saat")

    
    urgent_need = models.TextField("Acil İhtiyaçlar", blank=True)
    map_link = models.URLField("Harita Linki", blank=True)
    active = models.BooleanField("Aktif mi?", default=True)
    updated_at = models.DateTimeField("Son Güncelleme", auto_now=True)

    class Meta:
        verbose_name = "Bağış Merkezi"
        verbose_name_plural = "Bağış Merkezleri"

    def occupancy_percent(self):
        if self.capacity == 0:
            return 0
        return int((self.current_load / self.capacity) * 100)

    def remaining_capacity(self):
        remaining = self.capacity - self.current_load

        if remaining < 0:
            return 0

        return remaining

    def __str__(self):
        return f"{self.name} ({self.city})"

class Donation(models.Model):
    DONATION_TYPES = [
        ("para", "Para Bağışı"),
        ("urun", "Ürün Bağışı"),
    ]

    campaign = models.ForeignKey(
        Campaign,
        on_delete=models.CASCADE,
        related_name="donations",
        verbose_name="Kampanya"
    )

    full_name = models.CharField("Ad Soyad", max_length=150)
    email = models.EmailField("E-Posta", blank=True)
    phone = models.CharField("Telefon", max_length=30, blank=True)

    donation_type = models.CharField(
        "Bağış Türü",
        max_length=20,
        choices=DONATION_TYPES
    )

    amount = models.DecimalField(
        "Tutar",
        max_digits=10,
        decimal_places=2,
        default=0
    )

    product_description = models.TextField("Ürün Bağışı Açıklaması", blank=True)
    message = models.TextField("Not", blank=True)
    created_at = models.DateTimeField("Bağış Tarihi", auto_now_add=True)

    class Meta:
        verbose_name = "Bağış"
        verbose_name_plural = "Bağışlar"

    def __str__(self):
        return f"{self.full_name} - {self.campaign.title}"    