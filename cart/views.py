from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart
from customers.models import Customer
from orders.models import Order, OrderItem


@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(
        user=request.user
    )

    items = cart.items.all()

    total = 0

    for item in items:
        total += item.product.price * item.quantity

    return render(
        request,
        "cart.html",
        {
            "cart": cart,
            "items": items,
            "total": total,
        }
    )


@login_required
def checkout(request):
    cart, created = Cart.objects.get_or_create(
        user=request.user
    )

    items = cart.items.all()

    if not items.exists():
        return redirect("cart_detail")

    total = 0

    for item in items:
        total += item.product.price * item.quantity

    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        city = request.POST.get("city")
        address = request.POST.get("address")

        customer, created = Customer.objects.get_or_create(
            email=email,
            defaults={
                "first_name": first_name,
                "last_name": last_name,
                "phone": phone,
                "city": city,
                "address": address,
            }
        )

        order = Order.objects.create(
    user=request.user,
    customer=customer,
    phone=phone,
    city=city,
    address=address,
    total_price=total,
)

        for item in items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                unit_price=item.product.price,
            )

            item.product.stock -= item.quantity
            item.product.save()

        items.delete()

        return redirect("order_success")

    return render(
        request,
        "checkout.html",
        {
            "items": items,
            "total": total,
        }
    )


@login_required
def order_success(request):
    return render(request, "order_success.html")