from django.db import models
from customers.models import Customer
from products.models import Product
from django.contrib.auth.models import User

class Order(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Beklemede"
        PREPARING = "preparing", "Hazırlanıyor"
        SHIPPED = "shipped", "Kargoya Verildi"
        DELIVERED = "delivered", "Teslim Edildi"
        CANCELLED = "cancelled", "İptal Edildi"

    user = models.ForeignKey(
        User,
        verbose_name="Kullanıcı",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders"
    )

    customer = models.ForeignKey(
        Customer,
        verbose_name="Müşteri",
        on_delete=models.CASCADE,
        related_name="orders"
    )

    status = models.CharField(
        "Sipariş Durumu",
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )

    address = models.TextField("Teslimat Adresi")
    city = models.CharField("Şehir", max_length=100)
    phone = models.CharField("Telefon", max_length=20)

    total_price = models.DecimalField(
        "Toplam Tutar",
        max_digits=10,
        decimal_places=2,
        default=0
    )

    created_at = models.DateTimeField(
        "Sipariş Tarihi",
        auto_now_add=True
    )

    class Meta:
        verbose_name = "Sipariş"
        verbose_name_plural = "Siparişler"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Sipariş #{self.id} - {self.customer}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        verbose_name="Sipariş",
        on_delete=models.CASCADE,
        related_name="items"
    )

    product = models.ForeignKey(
        Product,
        verbose_name="Ürün",
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField("Adet", default=1)

    unit_price = models.DecimalField(
        "Birim Fiyat",
        max_digits=10,
        decimal_places=2
    )

    class Meta:
        verbose_name = "Sipariş Kalemi"
        verbose_name_plural = "Sipariş Kalemleri"

    def line_total(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return f"{self.product} x {self.quantity}"