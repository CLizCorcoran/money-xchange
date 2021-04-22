import re
from django.utils.timezone import datetime
from datetime import date
from django.shortcuts import render
from django.shortcuts import redirect
from store.forms import TransactionForm, BuyForm
from store.models import Transactions, Portfolio
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponse

from .models import Cryptocurrency

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

    #bitcoin = quandl.get("BITFINEX/BTCUSD", start_date="2021-04-15", end_date="2021-04-15")
    #ethereum = quandl.get("BITFINEX/ETHUSD", start_date="2021-04-15", end_date="2021-04-15")
    #ripple = quandl.get("BITFINEX/XRPUSD", start_date="2021-04-15", end_date="2021-04-15")
    #litecoin = quandl.get("BITFINEX/LTCUSD", start_date="2021-04-15", end_date="2021-04-15")
    #bitcoincash = quandl.get("BITFINEX/BCHUSD", start_date="2021-04-15", end_date="2021-04-15")
    #zcash = quandl.get("BITFINEX/ZECUSD", start_date="2021-04-15", end_date="2021-04-15")

    #currencies = Cryptocurrency.objects.all()
    #day = date.today() 
    #endDate = day.strftime("%Y-%m-%d")
    #startDate = str(day.year) + '-' + str(day.month-1) + '-' + str(day.day)
    #fromDate = "2021-04-01"
    for currency in Cryptocurrency.objects.all():
        name = "BITFINEX/" + currency.symbol + "USD"
        #info = quandl.get(name, start_date=startDate, end_date=endDate)
        info = quandl.get(name, rows=1)
        currency.price = info.Last.values[0]
        currency.save()

    cryptos = Cryptocurrency.objects.all()
    context = {
        'cryptos': cryptos
    }

    return render(request, 'store/home.html', context)

    #return render(
    #    request,
    #    'store/home.html',
    #    {
    #        'date': datetime.now(),
    #        'bitcoin': bitcoin.Last.values[0],
    #        'ethereum': ethereum.Last.values[0],
    #        'ripple': ripple.Last.values[0],
    #        'litecoin': litecoin.Last.values[0],
     #       'zcash': zcash.Last.values[0],
    #        #'bitcoincash': bitcoincash.Last.values[0]
     #   }
    #)
    
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


def buy(request, symbol):

    info = Cryptocurrency.objects.get(symbol=symbol)
        
    if request.method == "POST":
        form = BuyForm(request.POST, initial={'quantity': 0})
        
        if form.is_valid():
            quantity = form.cleaned_data.get('quantity')
            transaction = Transactions(user=request.user, symbol=info.symbol, price=info.price, log_date=datetime.now(), action='b', quantity=quantity)
            transaction.save()

            try:
                entry = Portfolio.objects.get(symbol=symbol)
                entry.quantity += quantity
                entry.save()
            
            except Portfolio.DoesNotExist:
                # The get method throws this when query fails
                entry = Portfolio(user=request.user, symbol=info.symbol, quantity=quantity)
                entry.save()

            return render(request, 'store/buy_complete.html')

    else:
        form = BuyForm()
        
        context = {
            'crypto': info,
            'form': form
        }
        return render( request, 'store/buy.html', context )



 

