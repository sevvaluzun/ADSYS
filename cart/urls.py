from django.urls import path
from .views import cart_detail, checkout, order_success

urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('odeme/', checkout, name='checkout'),
    path('siparis-basarili/', order_success, name='order_success'),
]