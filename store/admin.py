from django.contrib import admin
from .models import Transactions, Account, Cryptocurrency, Portfolio

admin.site.register(Transactions)
admin.site.register(Account)
admin.site.register(Cryptocurrency)
admin.site.register(Portfolio)