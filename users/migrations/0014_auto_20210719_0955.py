# Generated by Django 3.0.4 on 2021-07-19 04:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0013_auto_20210706_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesperson',
            name='assigned_freelancer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='freelancer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='freelancer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
