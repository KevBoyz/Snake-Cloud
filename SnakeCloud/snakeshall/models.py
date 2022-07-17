from django.db import models
from django_quill.fields import QuillField


class QuillPost(models.Model):
    name = models.TextField(blank=True, default='test')
    content = QuillField()

    def __str__(self):
        return self.name
