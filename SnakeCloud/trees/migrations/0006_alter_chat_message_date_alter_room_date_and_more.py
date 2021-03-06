# Generated by Django 4.0.6 on 2022-07-15 21:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0005_chat_message_alter_room_date_delete_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat_message',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 15, 18, 56, 26, 152131)),
        ),
        migrations.AlterField(
            model_name='room',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 15, 18, 56, 26, 152131)),
        ),
        migrations.AlterField(
            model_name='room',
            name='users',
            field=models.JSONField(default=dict),
        ),
    ]
