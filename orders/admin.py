from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "customer",
        "status",
        "city",
        "total_price",
        "created_at",
    )

    list_filter = (
        "status",
        "city",
        "created_at",
    )

    search_fields = (
        "customer__first_name",
        "customer__last_name",
        "customer__email",
        "phone",
    )

    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "order",
        "product",
        "quantity",
        "unit_price",
        "line_total",
    )
