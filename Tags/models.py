from django.db import models

from taggit.managers import TaggableManager


class Tags(models.Model):
    languages = models.CharField(max_length=50, verbose_name='Knowledge & skills')
    tags = TaggableManager()

    def __str__(self):
        return self.languages

class Users(models.Model):
    user_name = models.CharField(max_length=50, verbose_name='User name')
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE, verbose_name='Knowledge & skills')

    def __str__(self):
        return self.user_name

class Company(models.Model):
    departments = models.CharField(max_length=200)
    domain = models.CharField(max_length=200)

    def __str__(self):
        return self.departments
