from django.contrib import admin
from .models import Campaign, Volunteer
from .models import Campaign, Volunteer, PreparednessCheck, DonationCenter

@admin.register(DonationCenter)
class DonationCenterAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "city",
        "campaign",
        "capacity",
        "current_load",
        "status",
        "active",
        "updated_at",
        "latitude",
        "longitude",
    )

    list_filter = (
        "city",
        "status",
        "active",
        "campaign",
    )

    search_fields = (
        "name",
        "city",
        "address",
        "manager",
        "phone",
        "urgent_need",
    )