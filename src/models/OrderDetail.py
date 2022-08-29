from datetime import datetime
from django.db import models

from .Order import Order
from .Ticket import Ticket

# Create your models here.


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.RESTRICT)
    quantity = models.IntegerField(default=0)
    data = models.TextField(null=True)
    created_at = models.DateTimeField(null=True,auto_now_add=True)
    updated_at = models.DateTimeField(null=True,auto_now=True)
