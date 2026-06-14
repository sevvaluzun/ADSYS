from django.urls import path
from .views import (
    donation_home,
    information,
    volunteer,
    volunteer_success,
    preparedness_check,
    donation_create,
    donation_success,
    disaster_detail,
)

urlpatterns = [
    path("", donation_home, name="donation_home"),
    path("bilgi/", information, name="information"),
    path("gonullu/", volunteer, name="volunteer"),
    path("gonullu/basarili/", volunteer_success, name="volunteer_success"),
    path("hazirlik-kontrolu/", preparedness_check, name="preparedness_check"),

    path("bagis-yap/", donation_create, name="donation_create"),
    path("bagis-basarili/", donation_success, name="donation_success"),

    path("<slug:slug>/", disaster_detail, name="disaster_detail"),
]