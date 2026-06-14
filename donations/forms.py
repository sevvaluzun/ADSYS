from django import forms
from .models import Volunteer
from .models import PreparednessCheck

class VolunteerForm(forms.ModelForm):

    class Meta:
        model = Volunteer

        fields = "__all__"

        widgets = {

            "full_name": forms.TextInput(attrs={"class":"form-control"}),

            "phone": forms.TextInput(attrs={"class":"form-control"}),

            "email": forms.EmailInput(attrs={"class":"form-control"}),

            "city": forms.TextInput(attrs={"class":"form-control"}),

            "support_area": forms.Select(attrs={"class":"form-select"}),

            "message": forms.Textarea(
                attrs={
                    "class":"form-control",
                    "rows":4
                }
            )

        }
class PreparednessCheckForm(forms.ModelForm):
    class Meta:
        model = PreparednessCheck
        fields = [
            "emergency_bag",
            "meeting_area",
            "first_aid",
            "family_plan",
            "emergency_numbers",
            "powerbank",
            "flashlight",
            "water_food",
        ]

        widgets = {
            "emergency_bag": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "meeting_area": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "first_aid": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "family_plan": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "emergency_numbers": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "powerbank": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "flashlight": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "water_food": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

from .models import Donation


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = [
            "campaign",
            "full_name",
            "email",
            "phone",
            "donation_type",
            "amount",
            "product_description",
            "message",
        ]

        widgets = {
            "campaign": forms.Select(attrs={"class": "form-select"}),
            "full_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "donation_type": forms.Select(attrs={"class": "form-select"}),
            "amount": forms.NumberInput(attrs={"class": "form-control"}),
            "product_description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3
            }),
            "message": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3
            }),
        }

from .models import Donation


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = [
            "campaign",
            "full_name",
            "email",
            "phone",
            "donation_type",
            "amount",
            "product_description",
            "message",
        ]

        widgets = {
            "campaign": forms.Select(attrs={"class": "form-select"}),
            "full_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "donation_type": forms.Select(attrs={"class": "form-select", "id": "donationType"}),
            "amount": forms.NumberInput(attrs={"class": "form-control", "min": "0"}),
            "product_description": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "message": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }