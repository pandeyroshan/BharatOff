# Generated by Django 3.0.4 on 2021-08-26 04:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0014_auto_20210826_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='end_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 8, 26, 10, 7, 44, 200976)),
        ),
    ]