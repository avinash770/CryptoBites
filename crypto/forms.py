from django import forms
from .models import Coin, BuyCoins


# Creating user form to place order
class BuyCoinsForm(forms.ModelForm):
    class Meta:
        model = BuyCoins
        fields = ['customerName', 'qty', 'address', 'price', 'email', 'name']
        labels = {'customerName': 'Enter your legal name', 'qty': 'Quantity', 'address': 'Enter your wallet address',
                  'price': 'Current Price', 'email': 'Enter your email ID', 'name': 'Select Coin'}
