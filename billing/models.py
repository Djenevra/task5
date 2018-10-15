from django.db import models



class CurrencyCirculation(models.Model):
    user = models.ForeignKey('users.User', on_delete = models.CASCADE)
    task = models.ForeignKey('tasks.Task', on_delete = models.CASCADE, default=None, null=True)
    reason = models.CharField(max_length=255)
    debit = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    credit = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    currency = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    balance = models.DecimalField(max_digits=7, decimal_places=2, default=0)


class TaskRelatedNotes(models.Model):
    task = models.ForeignKey('tasks.Task', on_delete = models.CASCADE)
    executor = models.ForeignKey('users.User', on_delete = models.CASCADE)
    money = models.DecimalField(max_digits=7, decimal_places=2, default=0)
