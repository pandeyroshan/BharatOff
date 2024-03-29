# Generated by Django 3.0.4 on 2021-08-23 02:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('management', '0007_auto_20210822_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='couponhistory',
            name='ad',
        ),
        migrations.RemoveField(
            model_name='couponhistory',
            name='code',
        ),
        migrations.RemoveField(
            model_name='couponhistory',
            name='expiry_date',
        ),
        migrations.RemoveField(
            model_name='couponhistory',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='couponhistory',
            name='coupon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='management.Coupon'),
        ),
        migrations.AddField(
            model_name='couponhistory',
            name='is_redeemed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='end_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 8, 23, 8, 2, 41, 365908)),
        ),
        migrations.AlterField(
            model_name='couponhistory',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='couponhistory',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
