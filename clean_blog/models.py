from django.db import models

# Create your models here.
from mdeditor.fields import MDTextField
from taggit.managers import TaggableManager


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    category = models.TextField()
    content = MDTextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    is_public = models.BooleanField(default=False)
    tags = TaggableManager()

    def __str__(self):
        return '%s, %s - %s' % (self.title, self.author, str(self.created_at).split('.')[0])
