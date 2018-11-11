from django.db import models


class TaskRelatedNotes(models.Model):
    task = models.ForeignKey('tasks.Task', on_delete=models.PROTECT)
    executor = models.ForeignKey('users.User', on_delete=models.PROTECT,
                                 default=None)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
