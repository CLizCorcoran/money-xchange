import re
from django.utils.timezone import datetime
from django.shortcuts import render
from django.shortcuts import redirect
from store.forms import TransactionForm
from store.models import Transactions
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponse

import quandl 
from .secrets import *


#class HomeListView(ListView):
#    """Renders the home page, with a list of all messages."""
#    model = Transactions 
#
#    def get_context_data(self, **kwargs):
#        context = super(HomeListView, self).get_context_data(**kwargs)
#        return context

def home(request):
    #return render(request, "store/home.html")
    # High, Low, Mid, Last, Bid, Ask, Volume
    quandl.ApiConfig.api_key = QUANDL_KEY

    bitcoin = quandl.get("BITFINEX/BTCUSD", start_date="2021-04-15", end_date="2021-04-15")
    ethereum = quandl.get("BITFINEX/ETHUSD", start_date="2021-04-15", end_date="2021-04-15")
    ripple = quandl.get("BITFINEX/XRPUSD", start_date="2021-04-15", end_date="2021-04-15")
    litecoin = quandl.get("BITFINEX/LTCUSD", start_date="2021-04-15", end_date="2021-04-15")
    #bitcoincash = quandl.get("BITFINEX/BCHUSD", start_date="2021-04-15", end_date="2021-04-15")
    zcash = quandl.get("BITFINEX/ZECUSD", start_date="2021-04-15", end_date="2021-04-15")

    return render(
        request,
        'store/home.html',
        {
            'date': datetime.now(),
            'bitcoin': bitcoin.Last.values[0],
            'ethereum': ethereum.Last.values[0],
            'ripple': ripple.Last.values[0],
            'litecoin': litecoin.Last.values[0],
            'zcash': zcash.Last.values[0],
            #'bitcoincash': bitcoincash.Last.values[0]
        }
    )
    
    #return HttpResponse(mydata.Last)

def about(request):
    return render(request, "store/about.html")

def contact(request):
    return render(request, "store/contact.html")

@login_required
def log_transaction(request):
    form = TransactionForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            symbol = form.save(commit=False)
            symbol.log_date = datetime.now()
            symbol.save()
            return redirect("home")

    else:
        return render(request, "store/transaction.html", {"form":form})

class TransactionsByUserListView(LoginRequiredMixin, ListView):
    """Generic class-based view listing transactions from the current user"""
    model = Transactions
    template_name = 'store/transactions_list_user.html'
    paginate_by = 10

    # can also specify a filter(var=value)
    def get_queryset(self):
        return Transactions.objects.filter(user=self.request.user).order_by('log_date')

def stock_info(request, name):
    return render(
        request,
        'store/stock_info.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )



 

