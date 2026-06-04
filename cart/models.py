from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Cart(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name="Kullanıcı",
        on_delete=models.CASCADE,
        related_name="cart",
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        "Oluşturulma Tarihi",
        auto_now_add=True
    )

    class Meta:
        verbose_name = "Sepet"
        verbose_name_plural = "Sepetler"

    def __str__(self):
        if self.user:
            return f"{self.user.username} Sepeti"
        return f"Sepet #{self.id}"


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name="Sepet"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Ürün"
    )

    quantity = models.PositiveIntegerField(
        "Adet",
        default=1
    )

    class Meta:
        verbose_name = "Sepet Kalemi"
        verbose_name_plural = "Sepet Kalemleri"

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"