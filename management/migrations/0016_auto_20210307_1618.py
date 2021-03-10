# Generated by Django 3.0.4 on 2021-03-07 10:48

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('management', '0015_auto_20210307_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='couponhistory',
            name='expiry_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='files',
            name='rated_by',
            field=models.ManyToManyField(blank=True, related_name='rated_by', to=settings.AUTH_USER_MODEL),
        ),
    ]