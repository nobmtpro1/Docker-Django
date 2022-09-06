from ..models import Course, CourseCategory
import random


def seed():
    Course.objects.all().delete()

    courseCategories = CourseCategory.objects.filter()

    Course.objects.bulk_create(
        [
            Course(
                name="Course " + str(x),
                price=1000000 * x,
                course_category_id=random.randint(
                    courseCategories.first().id, courseCategories.last().id
                ),
            )
            for x in range(1, 20)
        ]
    )
