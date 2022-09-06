from dataclasses import fields
from ..models import CourseCategory, Course, Session
from .DynamicFieldsModelSerializer import DynamicFieldsModelSerializer


class CourseCategorySerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = CourseCategory
        fields = "__all__"


class SessionSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Session
        fields = "__all__"


class CourseSerializer(DynamicFieldsModelSerializer):
    sessions = SessionSerializer(source="session_set", many=True, read_only=True)
    course_category = CourseCategorySerializer(many=False, read_only=True)

    class Meta:
        model = Course
        fields = "__all__"
