from django.db import models
from django.utils import timezone

class Transactions(models.Model):
    symbol = models.CharField(max_length=3)
    log_date = models.DateTimeField("date logged")
    user_id = models.IntegerField()
    action = models.IntegerField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        """Returns a string representation of a transaction"""
        date = timezone.localtime(self.log_date)
        if action == 1:
            return f"'{symbol}' was purchased on {date.strftime('%a, %d %B, %y at %X')}.  {quantity} shares were purchased at ${price} per share.  User:  {user_id}"

        elif action == 2:
            return f"'{symbol}' was sold on {date.strftime('%a, %d %B, %y at %X')}.  {quantity} shares were sold at ${price} per share.  User:  {user_id}"



