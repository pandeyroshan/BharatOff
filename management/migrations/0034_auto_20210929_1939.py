# Generated by Django 3.0.4 on 2021-09-29 14:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0033_auto_20210929_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='end_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 9, 29, 19, 39, 15, 507182)),
        ),
    ]