# Generated by Django 3.0.4 on 2021-01-19 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0007_coupon_couponhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]