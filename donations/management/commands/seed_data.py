from django.core.management.base import BaseCommand
from products.models import Category, Supplier, Product
from donations.models import Campaign, DonationCenter


class Command(BaseCommand):
    help = "ADSYS başlangıç verilerini oluşturur"

    def handle(self, *args, **kwargs):
        supplier, _ = Supplier.objects.get_or_create(
            name="ADSYS Tedarik"
        )

        products = [
            ("Afet Çantaları", "Deprem Çantası", 899, 25, "Temel afet hazırlığı için çok amaçlı deprem çantası."),
            ("Afet Çantaları", "Düdük", 49, 80, "Acil durumda sesinizi duyurmak için güvenlik düdüğü."),
            ("Afet Çantaları", "Isı Battaniyesi", 89, 60, "Vücut ısısını korumaya yardımcı acil durum battaniyesi."),
            ("Afet Çantaları", "Su Geçirmez Çanta", 349, 30, "Acil malzemeleri korumak için su geçirmez çanta."),

            ("İlk Yardım", "İlk Yardım Seti", 399, 40, "Ev, okul ve iş yeri için temel ilk yardım malzemeleri."),
            ("İlk Yardım", "Steril Gazlı Bez", 45, 100, "Yara kapatma için steril gazlı bez."),
            ("İlk Yardım", "Elastik Bandaj", 65, 80, "Burkulma ve incinmelerde destek amaçlı bandaj."),
            ("İlk Yardım", "Yara Bandı Paketi", 35, 120, "Küçük yaralar için yara bandı paketi."),
            ("İlk Yardım", "Antiseptik Solüsyon", 89, 70, "Yara çevresi temizliği için antiseptik solüsyon."),
            ("İlk Yardım", "Tek Kullanımlık Eldiven", 49, 90, "Hijyenik müdahale için tek kullanımlık eldiven."),

            ("Aydınlatma ve Enerji", "El Feneri", 199, 50, "Afet ve elektrik kesintileri için güçlü LED el feneri."),
            ("Aydınlatma ve Enerji", "Powerbank", 549, 30, "Acil durumlarda taşınabilir enerji kaynağı."),
            ("Aydınlatma ve Enerji", "Kafa Lambası", 249, 40, "Karanlıkta eller serbest kullanım için kafa lambası."),
            ("Aydınlatma ve Enerji", "Şarjlı Fener", 329, 35, "Uzun süreli aydınlatma için şarjlı fener."),
            ("Aydınlatma ve Enerji", "AA Pil Paketi", 79, 100, "El feneri ve cihazlar için AA pil paketi."),
            ("Aydınlatma ve Enerji", "AAA Pil Paketi", 69, 100, "Küçük cihazlar için AAA pil paketi."),

            ("Gıda ve Su", "Konserve Gıda Paketi", 249, 35, "Uzun ömürlü afet gıda desteği paketi."),
            ("Gıda ve Su", "Acil Su Paketi", 129, 45, "Afet sonrası temel su ihtiyacı için hazırlanmış paket."),
            ("Gıda ve Su", "Enerji Barı", 39, 150, "Acil durumlar için yüksek enerjili bar."),
            ("Gıda ve Su", "Hazır Çorba Paketi", 59, 110, "Kolay hazırlanabilir uzun ömürlü gıda."),
            ("Gıda ve Su", "Kuru Meyve Paketi", 89, 80, "Besleyici ve dayanıklı kuru meyve paketi."),

            ("Hijyen", "Hijyen Seti", 299, 28, "Temel hijyen ürünlerinden oluşan afet seti."),
            ("Hijyen", "Islak Mendil", 39, 150, "Temel hijyen için ıslak mendil."),
            ("Hijyen", "Dezenfektan", 69, 120, "El ve yüzey temizliği için dezenfektan."),
            ("Hijyen", "Maske Paketi", 49, 100, "Toz ve kalabalık alanlar için maske paketi."),
            ("Hijyen", "Kadın Hijyen Paketi", 119, 60, "Afet dönemlerinde temel hijyen ihtiyaçları."),

            ("Yangın Güvenliği", "Yangın Söndürücü", 749, 12, "Ev ve iş yerleri için temel yangın güvenliği ürünü."),
            ("Yangın Güvenliği", "Yangın Battaniyesi", 249, 35, "Küçük yangınlarda boğma amaçlı yangın battaniyesi."),
            ("Yangın Güvenliği", "Duman Dedektörü", 399, 25, "Ev ve iş yerleri için duman algılama cihazı."),
            ("Yangın Güvenliği", "Gaz Kaçak Dedektörü", 549, 20, "Gaz kaçağı riskine karşı uyarı cihazı."),

            ("Bebek", "Bebek Bezi", 179, 70, "Afet bölgesi ve aile ihtiyaçları için bebek bezi."),
            ("Bebek", "Bebek Maması", 149, 50, "Afet dönemlerinde bebekler için mama desteği."),
            ("Bebek", "Biberon", 89, 50, "Bebek beslenmesi için biberon."),

            ("Evcil Hayvan", "Kedi Maması", 129, 45, "Tahliye ve acil durumlar için kedi maması."),
            ("Evcil Hayvan", "Köpek Maması", 149, 45, "Tahliye ve acil durumlar için köpek maması."),
            ("Evcil Hayvan", "Katlanabilir Mama Kabı", 99, 40, "Evcil hayvanlar için taşınabilir mama kabı."),

            ("Kurtarma ve Güvenlik", "Koruyucu Eldiven", 119, 60, "Enkaz ve taşıma işlemleri için koruyucu eldiven."),
            ("Kurtarma ve Güvenlik", "Toz Maskesi", 49, 90, "Tozlu ortamlarda solunum koruması."),
            ("Kurtarma ve Güvenlik", "Reflektörlü Yelek", 159, 50, "Gece ve kalabalık alanlarda görünürlük sağlar."),

            ("Barınma", "Uyku Tulumu", 699, 25, "Tahliye ve geçici barınma için uyku tulumu."),
            ("Barınma", "Katlanabilir Mat", 249, 35, "Geçici barınmada zemin izolasyonu sağlar."),
            ("Barınma", "Yağmurluk", 159, 60, "Yağışlı havalarda koruma sağlar."),
            ("Barınma", "Termal Çorap", 79, 80, "Soğuk hava koşullarında sıcak tutar."),
        ]

        for category_name, name, price, stock, description in products:
            category, _ = Category.objects.get_or_create(name=category_name)

            Product.objects.get_or_create(
                name=name,
                defaults={
                    "category": category,
                    "supplier": supplier,
                    "description": description,
                    "price": price,
                    "cost_price": int(price * 0.6),
                    "stock": stock,
                    "minimum_stock": 5,
                    "is_active": True,
                }
            )

        campaign, _ = Campaign.objects.get_or_create(
            title="İstanbul Afet Yardım Kampanyası",
            defaults={
                "location": "İstanbul",
                "description": "Afet bölgelerine ulaştırılmak üzere temel ihtiyaç malzemeleri ve destek kampanyası.",
                "target_amount": 500000,
                "collected_amount": 125000,
                "needs": "Battaniye, su, konserve, hijyen seti, bebek bezi",
                "official_link": "https://www.afad.gov.tr",
                "active": True,
            }
        )

        centers = [
            {
                "name": "İstanbul Avrupa Yakası Lojistik Merkezi",
                "city": "İstanbul / Başakşehir",
                "address": "Başakşehir Afet Koordinasyon Alanı",
                "capacity": 1000,
                "current_load": 780,
                "status": "orta",
                "manager": "İstanbul Koordinasyon Ekibi",
                "phone": "0212 000 00 00",
                "working_hours": "24 Saat",
                "urgent_need": "Battaniye\nKonserve\nHijyen seti\nBebek bezi",
                "latitude": 41.0931,
                "longitude": 28.8020,
                "map_link": "https://www.google.com/maps",
            },
            {
                "name": "İstanbul Anadolu Yakası Yardım Merkezi",
                "city": "İstanbul / Ümraniye",
                "address": "Ümraniye Lojistik Destek Noktası",
                "capacity": 800,
                "current_load": 320,
                "status": "dusuk",
                "manager": "Anadolu Yakası Destek Ekibi",
                "phone": "0216 000 00 00",
                "working_hours": "09:00 - 22:00",
                "urgent_need": "Su\nKuru gıda\nİlk yardım malzemesi",
                "latitude": 41.0164,
                "longitude": 29.1248,
                "map_link": "https://www.google.com/maps",
            },
            {
                "name": "İstanbul Kritik Yardım Kabul Merkezi",
                "city": "İstanbul / Esenler",
                "address": "Esenler Afet Yardım Toplama Alanı",
                "capacity": 600,
                "current_load": 570,
                "status": "kritik",
                "manager": "Kriz Lojistik Ekibi",
                "phone": "0212 111 11 11",
                "working_hours": "24 Saat",
                "urgent_need": "Çadır\nIsıtıcı\nBattaniye",
                "latitude": 41.0435,
                "longitude": 28.8763,
                "map_link": "https://www.google.com/maps",
            },
        ]

        for center in centers:
            DonationCenter.objects.get_or_create(
                name=center["name"],
                defaults={
                    "campaign": campaign,
                    **center,
                }
            )

        self.stdout.write(self.style.SUCCESS("ADSYS seed verileri başarıyla oluşturuldu."))