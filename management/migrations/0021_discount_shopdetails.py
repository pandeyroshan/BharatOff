# Generated by Django 3.0.4 on 2021-07-05 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0020_files_comes_under'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_purchase', models.IntegerField(default=0)),
                ('discount', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Discount',
                'verbose_name_plural': 'Discount',
            },
        ),
        migrations.CreateModel(
            name='ShopDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=1000)),
                ('owner_name', models.CharField(max_length=1000)),
                ('phone_number', models.IntegerField(default=1)),
                ('whatsapp_number', models.IntegerField(default=1)),
                ('address', models.CharField(max_length=1000)),
                ('city', models.CharField(max_length=100)),
                ('email_address', models.CharField(max_length=1000)),
                ('business_category', models.CharField(max_length=1000)),
                ('products', models.TextField()),
                ('total_eligible_customer', models.IntegerField(default=0)),
                ('package_amount', models.IntegerField(default=1)),
                ('transaction_id', models.CharField(max_length=1000)),
                ('discounts', models.ManyToManyField(to='management.Discount')),
            ],
            options={
                'verbose_name': 'Shop Informations',
                'verbose_name_plural': 'Shop Informations',
            },
        ),
    ]