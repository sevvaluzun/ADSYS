from django.db import models


class Customer(models.Model):
    first_name = models.CharField(
        "Ad",
        max_length=100
    )

    last_name = models.CharField(
        "Soyad",
        max_length=100
    )

    email = models.EmailField(
        "E-Posta",
        unique=True
    )

    phone = models.CharField(
        "Telefon",
        max_length=20,
        blank=True
    )

    city = models.CharField(
        "Şehir",
        max_length=100,
        blank=True
    )

    address = models.TextField(
        "Adres",
        blank=True
    )

    created_at = models.DateTimeField(
        "Kayıt Tarihi",
        auto_now_add=True
    )

    class Meta:
        verbose_name = "Müşteri"
        verbose_name_plural = "Müşteriler"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"