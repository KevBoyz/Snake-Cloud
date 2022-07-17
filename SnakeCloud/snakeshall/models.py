from django.db import models
from django_quill.fields import QuillField
from django.contrib.auth.models import User
from datetime import datetime


class QuillPost(models.Model):
    title = models.TextField(default='')
    description = models.TextField(default='')
    admin = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    date = models.DateTimeField(blank=True, default=datetime.now())
    content = QuillField()

    def __str__(self):
        return self.title
