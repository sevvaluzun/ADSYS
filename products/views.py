from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Category
from cart.models import Cart, CartItem


def home(request):
    query = request.GET.get("q")
    category_id = request.GET.get("category")

    products = Product.objects.filter(is_active=True)
    categories = Category.objects.all()

    if query:
        products = products.filter(name__icontains=query)

    if category_id:
        products = products.filter(category_id=category_id)

    return render(
        request,
        "home.html",
        {
            "products": products,
            "categories": categories,
            "query": query,
            "selected_category": category_id,
        }
    )


@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)

    cart, created = Cart.objects.get_or_create(
        user=request.user
    )

    item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if not created:
        item.quantity += 1
        item.save()

    return redirect("home")