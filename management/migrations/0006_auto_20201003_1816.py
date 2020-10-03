# Generated by Django 3.0.4 on 2020-10-03 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_auto_20201003_1748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='files',
            name='MiniLocation',
        ),
        migrations.AddField(
            model_name='files',
            name='MiniLocation',
            field=models.ManyToManyField(to='management.MiniLocation'),
        ),
        migrations.RemoveField(
            model_name='files',
            name='city',
        ),
        migrations.AddField(
            model_name='files',
            name='city',
            field=models.ManyToManyField(to='management.CityData'),
        ),
    ]
