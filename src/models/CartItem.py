from datetime import datetime
from django.db import models
from .Course import Course
from .Session import Session
from .UserClient import UserClient

# Create your models here.


class CartItem(models.Model):
    user = models.ForeignKey(UserClient, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)
