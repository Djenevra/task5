from django.db import models
from django.contrib.auth.models import AbstractUser
from decimal import Decimal
from django.utils.translation import gettext as _
from billing.models import CurrencyCirculation
from django.db.models import F
from tasks.models import Task

class User(AbstractUser):
    PURCHASER = 1
    EXECUTOR = 2

    USER_TYPES = (
        (PURCHASER, _('purchaser')),
        (EXECUTOR, _('executor')),
    )

    name = models.CharField(blank = True, max_length = 255)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPES, default=EXECUTOR)
    balance = models.DecimalField(decimal_places = 2, max_digits = 7, default = 0)

    def __str__(self):
     return self.username

    def update_balance(self, set_price, executor_id, created_by_id):
        User.objects.select_for_update().filter(pk=created_by_id).update(
        balance=F('balance') - set_price)
        print ("executor id =", executor_id, "created_by id =", created_by_id)
        User.objects.select_for_update().filter(pk=executor_id).update(
        balance=F('balance') + set_price)
