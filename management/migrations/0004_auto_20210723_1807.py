# Generated by Django 3.0.4 on 2021-07-23 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_auto_20210723_1701'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filetest',
            options={'verbose_name': 'Testing Image File Upload', 'verbose_name_plural': 'Testing Image File'},
        ),
        migrations.AlterField(
            model_name='shopdetails',
            name='image_file1',
            field=models.ImageField(blank=True, null=True, upload_to='img/', verbose_name='Image 1'),
        ),
        migrations.AlterField(
            model_name='shopdetails',
            name='image_file2',
            field=models.ImageField(blank=True, null=True, upload_to='img/', verbose_name='Image 2'),
        ),
        migrations.AlterField(
            model_name='shopdetails',
            name='image_file3',
            field=models.ImageField(blank=True, null=True, upload_to='img/', verbose_name='Image 3'),
        ),
        migrations.AlterField(
            model_name='shopdetails',
            name='image_file4',
            field=models.ImageField(blank=True, null=True, upload_to='img/', verbose_name='Image 4'),
        ),
    ]