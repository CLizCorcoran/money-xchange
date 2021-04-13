import re
from django.utils.timezone import datetime
from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")

def stock_info(request, name):
    return render(
        request,
        'store/stock_info.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
 
        
