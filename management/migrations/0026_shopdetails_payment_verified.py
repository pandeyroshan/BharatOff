# Generated by Django 3.0.4 on 2021-07-19 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0025_auto_20210714_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopdetails',
            name='payment_verified',
            field=models.BooleanField(default=False),
        ),
    ]