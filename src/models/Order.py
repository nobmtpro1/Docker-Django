from datetime import datetime
from django.db import models

# Create your models here.


class Order(models.Model):
    name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    payment = models.CharField(max_length=255, default="bank")
    total = models.BigIntegerField(default=0)
    is_paid = models.IntegerField(default=0)
    created_at = models.DateTimeField(null=True,auto_now_add=True)
    updated_at = models.DateTimeField(null=True,auto_now=True)
