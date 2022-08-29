from datetime import datetime
from django.db import models

# Create your models here.


class Ticket(models.Model):
    type = models.CharField(max_length=255,default="online")
    image = models.TextField(null=True)
    name = models.CharField(max_length=255,null=True)
    date = models.DateTimeField(null=True)
    _from = models.TimeField(null=True)
    to = models.TimeField(null=True)
    quantity = models.IntegerField(default=0)
    address = models.CharField(max_length=255,null=True)
    price = models.BigIntegerField(default=0)
    link_video = models.TextField(null=True)
    created_at = models.DateTimeField(null=True,auto_now_add=True)
    updated_at = models.DateTimeField(null=True,auto_now=True)
