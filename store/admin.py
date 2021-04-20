from django.contrib import admin
from .models import Transactions, Account

admin.site.register(Transactions)
admin.site.register(Account)