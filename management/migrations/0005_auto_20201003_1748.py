# Generated by Django 3.0.4 on 2020-10-03 12:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_auto_20200930_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='company_name',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='files',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
