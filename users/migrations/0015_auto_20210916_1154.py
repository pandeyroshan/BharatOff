# Generated by Django 3.0.4 on 2021-09-16 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20210904_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerlogin',
            name='latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='customerlogin',
            name='longitude',
            field=models.FloatField(default=0.0),
        ),
    ]