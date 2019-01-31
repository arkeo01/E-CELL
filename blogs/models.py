from django.db import models
from tinymce.models import HTMLField

class blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = HTMLField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:100]+"..."
