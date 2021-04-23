from django.db import models
from django.utils import timezone
import uuid # Required for unique transaction identification
from django.contrib.auth.models import User 
from django.db.models.signals import post_save
from django.dispatch import receiver

# Hooked Account to User via this article:  
#   https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=8)

    @receiver(post_save, sender=User)
    def create_user_account(sender, instance, created, **kwargs):
        if created:
            Account.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_account(sender, instance, **kwargs):
        instance.account.save()
        
    def __str__(self):
        """Returns a string representation of a user's account"""
        return f"User, {self.user}, has ${self.amount} left in their account"

class Cryptocurrency(models.Model):
    symbol = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length = 20)
    price = models.DecimalField(max_digits=7, decimal_places = 2)

    def __str__(self):
        """Returns a string representation of a cryptocurrency"""
        return f"Cryptocurrency, {self.name} ({self.symbol}), has a price of {self.price}."

class Portfolio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this portfolio entry") 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    symbol = models.ForeignKey(Cryptocurrency, to_field='symbol', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    @property
    def total_value(self):
        if self.quantity and self.symbol.price:
            return self.quantity * self.symbol.price
        else:
            return 0

    def __str__(self):
        """Return a string representation of a user's portfolio"""
        return f"User, {self.user}, has {self.quantity} of {self.symbol}"

class Transactions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this transaction")
    symbol = models.ForeignKey(Cryptocurrency, to_field='symbol', on_delete=models.CASCADE)
    log_date = models.DateTimeField("date logged")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    ACTION_VALUES = (
        ('b', "Buy"),
        ('s', "Sell"),
    )

    action = models.CharField(max_length=1, choices=ACTION_VALUES, blank=True, default="b", help_text="Transaction type:,")
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)

    @property
    def total_price(self):
        if self.price and self.quantity:
            return self.price * self.quantity
        else:
            return 0

 #   def buy(self, symbol):
 #          new_transaction = Transaction.objects.create(
 #              symbol='BTC',
 #              log_date = 
 #          )

    def __str__(self):
        """Returns a string representation of a transaction"""
        date = timezone.localtime(self.log_date)
        if self.action == 'b':
            return f"'{self.symbol}' was purchased on {date.strftime('%a, %d %B, %y at %X')}.  {self.quantity} shares were purchased at ${self.price} per share.  Total amount:  {self.total_price}  User:  {self.user}"

        elif self.action == 's':
            return f"'{self.symbol}' was sold on {date.strftime('%a, %d %B, %y at %X')}.  {self.quantity} shares were sold at ${self.price} per share.  Total amount: {self.total_price}  User:  {self.user}"



