# Generated by Django 2.1.2 on 2018-10-18 07:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20181018_0709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='executor',
            field=models.ForeignKey(blank=True, null=True, on_delete='users.User', related_name='executor', to=settings.AUTH_USER_MODEL),
        ),
    ]