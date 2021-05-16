# Generated by Django 3.0.4 on 2021-03-20 04:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('management', '0019_auto_20210320_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='comes_under',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comes_under', to=settings.AUTH_USER_MODEL, verbose_name='Salesperson'),
            preserve_default=False,
        ),
    ]
