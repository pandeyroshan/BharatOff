# Generated by Django 3.0.4 on 2021-03-21 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20210108_0740'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesperson',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]