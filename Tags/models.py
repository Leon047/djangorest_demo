from django.db import models

from taggit.managers import TaggableManager


class Tags(models.Model):
    tags = TaggableManager()

class Users(models.Model):
    users = models.CharField(max_length=200)
