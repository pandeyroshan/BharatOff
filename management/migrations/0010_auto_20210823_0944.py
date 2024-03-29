# Generated by Django 3.0.4 on 2021-08-23 04:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('management', '0009_auto_20210823_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='end_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 8, 23, 9, 44, 10, 704580)),
        ),
        migrations.CreateModel(
            name='PaymentIssue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('coupon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Coupon')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Files')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Payment Complaint',
            },
        ),
    ]
