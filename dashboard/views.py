from django.shortcuts import render
from products.models import Product
from customers.models import Customer
from orders.models import Order


def dashboard_home(request):
    total_products = Product.objects.count()
    total_customers = Customer.objects.count()
    total_orders = Order.objects.count()

    total_revenue = 0
    for order in Order.objects.all():
        total_revenue += order.total_price

    low_stock_products = Product.objects.filter(
        stock__lte=5
    )

    recent_orders = Order.objects.order_by("-created_at")[:5]

    return render(
        request,
        "dashboard.html",
        {
            "total_products": total_products,
            "total_customers": total_customers,
            "total_orders": total_orders,
            "total_revenue": total_revenue,
            "low_stock_products": low_stock_products,
            "recent_orders": recent_orders,
        }
    )