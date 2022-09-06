from ..models import Session, Course
import random


def seed():
    Session.objects.all().delete()

    courses = Course.objects.filter()

    array = []

    for x in range(1, 100):
        randInt = random.randint(courses.first().id, courses.last().id)
        course = Course.objects.filter(id=randInt).first()
        array.append(
            Session(
                name="Session " + str(x),
                price=100000 * x,
                course_category_id=course.course_category_id,
                course_id=randInt,
            )
        )

    Session.objects.bulk_create(array)
