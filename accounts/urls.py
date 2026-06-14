from django.urls import path
from .views import register, my_orders, order_detail

urlpatterns = [
    path('kayit/', register, name='register'),
    path('siparislerim/', my_orders, name='my_orders'),
    path('siparislerim/<int:order_id>/', order_detail, name='order_detail'),

]