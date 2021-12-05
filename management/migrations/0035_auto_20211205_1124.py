# Generated by Django 2.1 on 2021-12-05 05:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0034_auto_20210929_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='TermsCondition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': 'Terms and Condition',
                'verbose_name_plural': 'Terms and Condition',
            },
        ),
        migrations.AlterField(
            model_name='coupon',
            name='end_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 12, 5, 11, 24, 58, 232699)),
        ),
        migrations.AlterField(
            model_name='files',
            name='keywords',
            field=models.TextField(blank=True, help_text='Provide comma-seperated keywords. Example: mobile, smartphone, charger, earphone'),
        ),
    ]
