from django.db import models


class UserClient(models.Model):
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255, null=True)
