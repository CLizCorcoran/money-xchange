from django import forms
from store.models import Transactions

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ["symbol", 'price', 'quantity', 'action', 'user',]  #NOTE:  the trailing comma is required
        

class BuyForm(forms.Form):
    quantity = forms.IntegerField()

    quantity.widget.attrs.update({'id': 'quantity', 'onChange': 'calcTotal()'})
      


