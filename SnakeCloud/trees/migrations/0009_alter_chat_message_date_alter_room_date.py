# Generated by Django 4.0.6 on 2022-07-17 02:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0008_alter_chat_message_date_alter_room_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat_message',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 16, 23, 44, 36, 895298)),
        ),
        migrations.AlterField(
            model_name='room',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 16, 23, 44, 36, 895298)),
        ),
    ]
