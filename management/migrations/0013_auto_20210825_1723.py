# Generated by Django 3.0.4 on 2021-08-25 11:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0012_auto_20210823_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='end_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 8, 25, 17, 23, 0, 632754)),
        ),
    ]
