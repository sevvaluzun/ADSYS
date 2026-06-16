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


