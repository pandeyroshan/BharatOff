# Generated by Django 3.0.4 on 2021-09-08 10:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0029_auto_20210908_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='pamphletdesign',
            name='total_downloads',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='end_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 9, 8, 15, 40, 49, 639484)),
        ),
    ]