# Generated by Django 4.0.6 on 2022-07-17 02:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jungle_of_files', '0012_alter_filepost_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filepost',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 16, 23, 44, 36, 895298)),
        ),
    ]
