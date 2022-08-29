from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.CharField(max_length=255,unique=True)
    type = models.CharField(max_length=255,default="client")

    def getData():
        return User.type
