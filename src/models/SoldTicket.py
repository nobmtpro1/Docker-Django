from datetime import datetime
from django.db import models

from .Ticket import Ticket

# Create your models here.


class SoldTicket(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.RESTRICT)
    code = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    cookie = models.TextField(null=True)
    created_at = models.DateTimeField(null=True,auto_now_add=True)
    updated_at = models.DateTimeField(null=True,auto_now=True)
