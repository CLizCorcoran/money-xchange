from django import forms
from django.contrib.auth.models import User
from store.models import Transactions

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ["symbol", 'price', 'quantity', 'action', 'user',]  #NOTE:  the trailing comma is required


class BuyForm(forms.Form):
    quantity = forms.IntegerField()
    quantity.widget.attrs.update({'id': 'quantity', 'min': '0', 'value': '0', 'onChange': 'calcTotal()'})


class SearchForm(forms.Form):
    symbol = forms.CharField(max_length=3)
    symbol.widget.attrs.update({'id': 'symbol_search', 'class': 'form-control mr-sm-2'})
      


