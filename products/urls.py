from django.urls import path
from .views import landing, home, add_to_cart
from .views import landing, home, add_to_cart, product_detail
urlpatterns = [
    path('', landing, name='landing'),

    path('magaza/', home, name='home'),

    path(
        'sepete-ekle/<int:product_id>/',
        add_to_cart,
        name='add_to_cart'
    ),
    path(
    'urun/<int:product_id>/',
    product_detail,
    name='product_detail'
),
]
