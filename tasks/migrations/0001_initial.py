# Generated by Django 2.1.2 on 2018-10-31 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('set_price', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
            ],
        ),
    ]
