# Generated by Django 3.0.4 on 2021-03-07 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0016_auto_20210307_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='couponhistory',
            name='expiry_date',
            field=models.DateTimeField(),
        ),
    ]
