from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField("Kategori Adı", max_length=150)
    description = models.TextField("Kategori Açıklaması", blank=True)

    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategoriler"

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField("Tedarikçi Adı", max_length=200)
    phone = models.CharField("Telefon", max_length=30, blank=True)
    email = models.EmailField("E-Posta", blank=True)
    address = models.TextField("Adres", blank=True)

    class Meta:
        verbose_name = "Tedarikçi"
        verbose_name_plural = "Tedarikçiler"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        verbose_name="Kategori",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products"
    )

    supplier = models.ForeignKey(
        Supplier,
        verbose_name="Tedarikçi",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products"
    )

    name = models.CharField(
        "Ürün Adı",
        max_length=200
    )

    description = models.TextField(
        "Ürün Açıklaması",
        blank=True
    )

    price = models.DecimalField(
        "Satış Fiyatı",
        max_digits=10,
        decimal_places=2
    )

    cost_price = models.DecimalField(
        "Alış Fiyatı",
        max_digits=10,
        decimal_places=2,
        default=0
    )

    stock = models.PositiveIntegerField(
        "Stok Miktarı",
        default=0
    )

    minimum_stock = models.PositiveIntegerField(
        "Minimum Stok Seviyesi",
        default=5
    )

    image = models.ImageField(
        "Ürün Görseli",
        upload_to="products/",
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        "Aktif",
        default=True
    )

    created_at = models.DateTimeField(
        "Oluşturulma Tarihi",
        auto_now_add=True
    )

    class Meta:
        verbose_name = "Ürün"
        verbose_name_plural = "Ürünler"
        ordering = ["name"]

    def __str__(self):
        return self.name

    from django.contrib.auth.models import User

class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "product")

    def __str__(self):
        return f"{self.user} - {self.product}"