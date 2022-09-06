from ..models import CourseCategory


def seed():
    CourseCategory.objects.all().delete()
    CourseCategory.objects.bulk_create(
        [
            CourseCategory(
                name="DIGITAL MARKETING",
            ),
            CourseCategory(
                name="ACCOUNT MANAGEMENT",
            ),
            CourseCategory(
                name="CREATIVE & CONTENT",
            ),
            CourseCategory(
                name="MARKETING MANAGEMENT",
            ),
            CourseCategory(
                name="EVENT & ACTIVATION",
            ),
        ]
    )
