# Generated by Django 3.0.4 on 2021-08-25 11:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0013_auto_20210825_1723'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_auto_20210813_1239'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationAlert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('total_reach', models.IntegerField(default=0)),
                ('minilocation', models.ManyToManyField(to='management.MiniLocation')),
                ('sent_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Notifications',
                'verbose_name_plural': 'Notifications',
            },
        ),
    ]