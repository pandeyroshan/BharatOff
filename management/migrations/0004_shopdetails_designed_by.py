# Generated by Django 3.0.4 on 2021-08-13 07:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('management', '0003_remove_files_designed_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopdetails',
            name='designed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='designed_by', to=settings.AUTH_USER_MODEL),
        ),
    ]