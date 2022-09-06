from datetime import datetime
from django.db import models
from .CourseCategory import CourseCategory

# Create your models here.


class Course(models.Model):
    course_category = models.ForeignKey(CourseCategory, on_delete=models.RESTRICT)
    name = models.CharField(max_length=255, null=True)
    price = models.IntegerField(default=0)
    is_active = models.IntegerField(default=1)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)
