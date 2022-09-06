from pprint import pprint
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.db.models import Prefetch

from ...serializers.CourseCategorySerializer import CourseCategorySerializer
from ...serializers.CourseSerializer import CourseSerializer
from ...models import Session, CourseCategory,Course


def index(request):

    # courseCategories = CourseCategory.objects.all()

    # serializer = CourseCategorySerializer(
    #     courseCategories, fields=("id", "name", "created_at", "courses","courses_with_sessions","sessions"), many=True
    # )

    courses = Course.objects.all()

    serializer = CourseSerializer(
        courses, many=True
    )

    return JsonResponse(serializer.data, safe=False)
