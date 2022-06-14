from django.db import models
from django.contrib.auth.models import AbstractUser
from taggit.managers import TaggableManager

class UserModel(AbstractUser):
    class Meta:
        db_table = 'users'

    introduce = models.TextField(max_length=500, null=True)
    genre = models.TextField(max_length=1000, blank=True)


# class User(models.Model):
#     name = models.CharField(max_length=100)
#
#     class Meta:
#         db_table = 'ReviewUser'
#
#     def __str__(self):
#         return self.name

