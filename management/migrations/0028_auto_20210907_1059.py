# Generated by Django 3.0.4 on 2021-09-07 05:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0027_auto_20210907_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='end_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 9, 7, 10, 59, 59, 191590)),
        ),
    ]
