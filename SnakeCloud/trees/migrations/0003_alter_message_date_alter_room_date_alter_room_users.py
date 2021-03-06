# Generated by Django 4.0.6 on 2022-07-15 21:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0002_rename_user_room_admin_room_date_room_users_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 15, 18, 11, 36, 271061)),
        ),
        migrations.AlterField(
            model_name='room',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 15, 18, 11, 36, 271061)),
        ),
        migrations.AlterField(
            model_name='room',
            name='users',
            field=models.JSONField(default='dict'),
        ),
    ]
