from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name
