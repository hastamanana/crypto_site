# forms.py

from django import forms
from .models import Asset, Purchase

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['name']

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['asset', 'quantity', 'price']
