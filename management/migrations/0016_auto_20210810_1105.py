# Generated by Django 3.0.4 on 2021-08-10 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0015_auto_20210810_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopdetails',
            name='business_category',
            field=models.CharField(max_length=1000),
        ),
    ]
