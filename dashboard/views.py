from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from products.models import Product
from orders.models import Order
from django.contrib.auth.models import User
from donations.models import Campaign, Volunteer


@login_required
def dashboard(request):

    context = {
        "product_count": Product.objects.count(),
        "order_count": Order.objects.count(),
        "user_count": User.objects.count(),
        "campaign_count": Campaign.objects.filter(active=True).count(),
        "volunteer_count": Volunteer.objects.count(),

        "low_stock": Product.objects.filter(stock__lte=5),
        "last_orders": Order.objects.order_by("-created_at")[:5],
        "last_campaigns": Campaign.objects.order_by("-created_at")[:5],
        "last_volunteers": Volunteer.objects.order_by("-created_at")[:5],
    }

    return render(request, "dashboard.html", context)