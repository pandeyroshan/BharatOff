# Generated by Django 3.0.4 on 2021-08-22 13:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_auto_20210822_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='end_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 8, 22, 19, 29, 43, 783901)),
        ),
    ]
