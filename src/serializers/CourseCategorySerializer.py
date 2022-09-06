from dataclasses import fields
from rest_framework import serializers
from ..models import CourseCategory, Course, Session
from .DynamicFieldsModelSerializer import DynamicFieldsModelSerializer


class SessionSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Session
        fields = "__all__"


class CourseSerializer(DynamicFieldsModelSerializer):
    session = SessionSerializer(source="session_set", many=True, read_only=True)

    class Meta:
        model = Course
        fields = "__all__"


class CourseCategorySerializer(DynamicFieldsModelSerializer):
    courses = CourseSerializer(source="course_set", many=True, read_only=True,fields=("id","name","price"))
    courses_with_sessions = CourseSerializer(
        source="course_set", many=True, read_only=True
    )
    sessions = CourseSerializer(source="session_set", many=True, read_only=True)

    class Meta:
        model = CourseCategory
        fields = "__all__"
