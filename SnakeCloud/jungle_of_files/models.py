from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class FilePost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    file = models.FileField(upload_to='jof')
    image = models.FileField(upload_to='jof/img', blank=True, default='jof/img/default.jpeg')
    date = models.DateTimeField(blank=True, default=datetime.now())

    def __str__(self):
        return self.title
