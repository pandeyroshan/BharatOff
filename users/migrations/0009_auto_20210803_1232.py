# Generated by Django 3.0.4 on 2021-08-03 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_shopkeeper_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freelancer',
            name='comes_under',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.SalesPerson'),
        ),
    ]
