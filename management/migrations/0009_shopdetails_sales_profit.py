# Generated by Django 3.0.4 on 2021-07-31 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0008_shopdetails_covered_under_monthly_reward'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopdetails',
            name='sales_profit',
            field=models.FloatField(default=0),
        ),
    ]
