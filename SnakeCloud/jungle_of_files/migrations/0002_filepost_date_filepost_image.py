# Generated by Django 4.0.6 on 2022-07-14 18:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jungle_of_files', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filepost',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 14, 15, 0, 10, 66370)),
        ),
        migrations.AddField(
            model_name='filepost',
            name='image',
            field=models.FileField(blank=True, default='jof/img/default.jpeg', upload_to='jof/img'),
        ),
    ]
