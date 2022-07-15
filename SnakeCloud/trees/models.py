from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Room(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField()
    description = models.TextField()
    date = models.DateTimeField(default=datetime.now(), blank=True)
    users = models.JSONField(default=dict)
    len = models.TextField()

    def __str__(self):
        return self.name


class Chat_message(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    message = models.TextField()
    date = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return f'{self.date} {self.user}: {self.message}'
