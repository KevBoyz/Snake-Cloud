# Generated by Django 4.0.6 on 2022-07-14 23:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jungle_of_files', '0003_alter_filepost_date_alter_filepost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filepost',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 14, 20, 6, 27, 788951)),
        ),
        migrations.AlterField(
            model_name='filepost',
            name='image',
            field=models.FileField(blank=True, default='jof/img/default.jpeg', upload_to='jof/img'),
        ),
    ]