from django import forms
from store.models import Transactions

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ["symbol", 'price', 'quantity', 'action', 'user',]    #NOTE:  the trailing comma is required