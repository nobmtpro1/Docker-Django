from datetime import datetime
from django.db import models

# Create your models here.


class CourseCategory(models.Model):
    name = models.CharField(max_length=255, null=True)
    is_active = models.IntegerField(default=1)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)
