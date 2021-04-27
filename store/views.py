import re
from django.utils.timezone import datetime
from datetime import date
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from store.forms import TransactionForm, BuyForm
from store.models import Account, Transactions, Portfolio
from django.views import generic 
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm


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
    date = datetime.now()
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
        'cryptos': cryptos,
        'date': date
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


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

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


class PortfolioByUserListView(LoginRequiredMixin, ListView):
    """Generic class-based view listing user's portfolio"""
    model = Portfolio
    template_name = 'store/portfolio.html'
    paginate_by = 10

    def get_queryset(self):
        #return Portfolio.objects.all().order_by('symbol')
        return Portfolio.objects.filter(user=self.request.user).order_by('symbol')

def stock_info(request, name):
    return render(
        request,
        'store/stock_info.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )


def transaction_complete(request):
    return render(request, 'store/transaction_complete.html')


def buy(request, symbol):

    info = Cryptocurrency.objects.get(symbol=symbol)
    account = Account.objects.get(user=request.user)
        
    if request.method == "POST":
        form = BuyForm(request.POST, initial={'quantity': 0})
        
        if form.is_valid():
            quantity = form.cleaned_data.get('quantity')

            # Save the Transaction
            transaction = Transactions(user=request.user, symbol=info, price=info.price, log_date=datetime.now(), action='b', quantity=quantity)
            transaction.save()

            # Update the User's account
            account.amount -= transaction.total_price
            account.save()

            # Add or Update the User's Portfolio entry.
            try:
                entry = Portfolio.objects.get(symbol=symbol)
                entry.quantity += quantity
                entry.save()
            
            except Portfolio.DoesNotExist:
                # The get method throws this when query fails
                entry = Portfolio(user=request.user, symbol=info, quantity=quantity)
                entry.save()

            context = {
                'balance': account.amount
            }
            return redirect('transaction_complete')

    else:
        form = BuyForm()
        
        context = {
            'crypto': info,
            'form': form
        }
        return render( request, 'store/buy.html', context )


def sell(request, symbol):
    info = Portfolio.objects.get(symbol=symbol)
    account = Account.objects.get(user=request.user)

    if request.method == "POST":
        form = BuyForm(request.POST, initial={'quantity': 0})
        
        if form.is_valid():
            quantity = form.cleaned_data.get('quantity')

            # Save the Transaction
            transaction = Transactions(user=request.user, symbol=info.symbol, price=info.symbol.price, log_date=datetime.now(), action='s', quantity=quantity)
            transaction.save()

            # Update the User's Account
            account.amount += transaction.total_price
            account.save()

            # Modify the User's Portfolio to reflect purchase.
            # Delete the Transaction if no coins are remaining.  
            entry = Portfolio.objects.get(symbol=symbol)
            entry.quantity -= quantity
            if quantity > 0:
                entry.save()
            else:
                entry.delete()   

            context = {
                'balance': account.amount
            }     
 
            return redirect('transaction_complete')

    else:
        form = BuyForm()
        
        context = {
            'crypto': info,
            'form': form
        }
        return render( request, 'store/sell.html', context )





 

