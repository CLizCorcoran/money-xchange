import re
from django.utils.timezone import datetime
from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return render(request, "store/home.html")
    #return HttpResponse("Hello, Django!")

def about(request):
    return render(request, "store/about.html")

def contact(request):
    return render(request, "store/contact.html")

def stock_info(request, name):
    return render(
        request,
        'store/stock_info.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
 

