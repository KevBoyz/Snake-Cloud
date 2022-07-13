from django.db import models
from django.contrib.auth.models import User


class FilePost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    file = models.FileField(upload_to='jof')
    # image_post = models.FileField(upload_to='jof/img')

    def __str__(self):
        return self.title
