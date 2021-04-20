from django.db import models
from django.utils import timezone
import uuid # Required for unique transaction identification
from django.contrib.auth.models import User 

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self):
        """Returns a string representation of a user's account"""
        return f"User, {self.user}, has ${self.amount} left in their account"


class Transactions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this transaction")
    symbol = models.CharField(max_length=3)
    log_date = models.DateTimeField("date logged")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    ACTION_VALUES = (
        ('b', "Buy"),
        ('s', "Sell"),
    )

    action = models.CharField(max_length=1, choices=ACTION_VALUES, blank=True, default="b", help_text="Transaction type:,")
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    @property
    def total_price(self):
        if self.price and self.quantity:
            return self.price * self.quantity
        else:
            return 0

    def __str__(self):
        """Returns a string representation of a transaction"""
        date = timezone.localtime(self.log_date)
        if self.action == 'b':
            return f"'{self.symbol}' was purchased on {date.strftime('%a, %d %B, %y at %X')}.  {self.quantity} shares were purchased at ${self.price} per share.  Total amount:  {self.total_price}  User:  {self.user}"

        elif self.action == 's':
            return f"'{self.symbol}' was sold on {date.strftime('%a, %d %B, %y at %X')}.  {self.quantity} shares were sold at ${self.price} per share.  Total amount: {self.total_price}  User:  {self.user}"



