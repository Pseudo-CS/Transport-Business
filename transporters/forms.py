# transporters/forms.py
from django import forms
from vendors.models import TransportOrder

class AcceptOrderForm(forms.ModelForm):
    class Meta:
        model = TransportOrder
        fields = ['quoted_price']
