# Generated by Django 3.0.4 on 2021-08-26 04:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0015_auto_20210826_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='end_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 8, 26, 10, 9, 58, 958143)),
        ),
    ]