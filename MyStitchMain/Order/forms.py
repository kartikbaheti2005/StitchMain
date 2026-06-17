from django import forms
from .models import Order
from cloths.models import UpperBody, LowerBody, buttonChoice, sleeveChoice, upperBodyChoice, lowerBodyChoice
from Auths.models import AppUser


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'status', 'days']
        widgets = {
            'days': forms.NumberInput(attrs={'min': 1}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].queryset = AppUser.objects.select_related('user').all()
        self.fields['customer'].label = "Customer"


class UpperBodyForm(forms.ModelForm):
    class Meta:
        model = UpperBody
        exclude = ['requirments']
        widgets = {
            'pocket': forms.CheckboxInput(),
        }


class LowerBodyForm(forms.ModelForm):
    class Meta:
        model = LowerBody
        exclude = ['requirements']