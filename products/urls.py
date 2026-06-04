from django.urls import path
from .views import home, add_to_cart

urlpatterns = [
    path('', home, name='home'),
    path(
        'sepete-ekle/<int:product_id>/',
        add_to_cart,
        name='add_to_cart'
    ),
]