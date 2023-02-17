from django import forms
from .models import NewAddress

class NewAddressForm(forms.ModelForm):
    class Meta:
        model = NewAddress
        fields = (
            'first_name',
            'last_name',
            'telephone',
            'street_address',
            'city',
            'state',
            'postal_code',
            'country',
        )