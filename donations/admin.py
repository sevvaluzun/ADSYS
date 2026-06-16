from django.contrib import admin
from .models import Campaign, Volunteer, PreparednessCheck, DonationCenter


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "location",
        "target_amount",
        "collected_amount",
        "active",
    )

    list_filter = (
        "active",
        "location",
    )

    search_fields = (
        "title",
        "location",
        "description",
    )


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


@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "city",
        "support_area",
        "phone",
    )


@admin.register(PreparednessCheck)
class PreparednessCheckAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "updated_at",
    )