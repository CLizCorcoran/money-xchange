import re
from django.utils.timezone import datetime
from django.shortcuts import render
from django.shortcuts import redirect
from store.forms import TransactionForm
from store.models import Transactions
from django.views.generic import ListView

from django.http import HttpResponse


class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = Transactions 

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

#def home(request):
    #return render(request, "store/home.html")
    #return HttpResponse("Hello, Django!")

def about(request):
    return render(request, "store/about.html")

def contact(request):
    return render(request, "store/contact.html")

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

def stock_info(request, name):
    return render(
        request,
        'store/stock_info.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )



 

