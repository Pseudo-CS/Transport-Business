# vendors/forms.py
from django import forms
from .models import TransportOrder

class TransportOrderForm(forms.ModelForm):
    class Meta:
        model = TransportOrder
        fields = ['product', 'quantity', 'pickup_location', 'destination']
