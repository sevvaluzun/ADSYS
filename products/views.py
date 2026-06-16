from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Product, Category
from cart.models import Cart, CartItem


ALLOWED_PRODUCT_IDS = [
    18, 13, 34, 25, 35, 24, 52, 77, 15, 32,
    53, 56, 10, 2, 46, 60, 20, 22, 61, 26,
    42, 16, 48, 40, 58, 43, 23, 62, 8, 57,
    45, 29, 9, 39, 50, 44, 47, 31, 64,
    51, 11, 49, 54, 17, 3
]


def landing(request):
    products = Product.objects.filter(
        id__in=ALLOWED_PRODUCT_IDS,
        is_active=True
    )[:4]

    return render(request, "landing.html", {"products": products})


def home(request):
    query = request.GET.get("q")
    category_id = request.GET.get("category")

    products = Product.objects.filter(
        id__in=ALLOWED_PRODUCT_IDS,
        is_active=True
    )

    categories = Category.objects.all()

    if query:
        products = products.filter(name__icontains=query)

    if category_id:
        products = products.filter(category_id=category_id)

    return render(request, "home.html", {
        "products": products,
        "categories": categories,
        "query": query,
        "selected_category": category_id,
    })


def product_detail(request, product_id):
    product = get_object_or_404(
        Product,
        id=product_id,
        id__in=ALLOWED_PRODUCT_IDS,
        is_active=True
    )

    related_products = Product.objects.filter(
        id__in=ALLOWED_PRODUCT_IDS,
        category=product.category,
        is_active=True
    ).exclude(id=product.id)[:4]

    return render(request, "product_detail.html", {
        "product": product,
        "related_products": related_products,
    })


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(
        Product,
        id=product_id,
        id__in=ALLOWED_PRODUCT_IDS,
        is_active=True
    )

    cart, created = Cart.objects.get_or_create(user=request.user)

    item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if not created:
        item.quantity += 1
        item.save()

    return redirect("home")