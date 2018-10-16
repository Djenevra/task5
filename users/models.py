from django.db import models
from django.contrib.auth.models import AbstractUser
from decimal import Decimal
from billing.models import CurrencyCirculation


class User(AbstractUser):
    PURCHASER = 1
    EXECUTOR = 2

    USER_TYPES = (
        (PURCHASER, 'purchaser'),
        (EXECUTOR, 'executor'))

    name = models.CharField(blank = True, max_length = 255)
    user_type = models.PositiveSmallIntegerField(choices = user_types,  default=EXECUTOR)
    balance = models.DecimalField(decimal_places = 2, max_digits = 7, default = 0)

    def __str__(self):
     return self.username

     def update_balance(self, reason, money, **kwargs):
        pass
        #updated_balance = {}
        #task = kwargs.get('task', None)
        #updated_balance['user'] = self
        #updated_balance['reason'] = reason
        #updated_balance['debit'] = abs(currency) if currency < 0 else 0
        #updated_balance['credit'] = abs(currency) if currency > 0 else 0
        #updated_balance['currency'] = currency
        #updated_balance['task'] = task
        #current_balance = User.objects.select_for_update().get(pk=self.pk).balance
        #updated_balance['balance'] = current_balance + Decimal(balance)

        #return updated_balance
