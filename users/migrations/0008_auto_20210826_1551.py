# Generated by Django 3.0.4 on 2021-08-26 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210826_1010'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notificationalert',
            old_name='minilocation',
            new_name='minilocations',
        ),
    ]
