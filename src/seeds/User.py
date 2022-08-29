from ..models import User


def seed():
    User.objects.all().delete()
    user = User(
        first_name="Administrator",
        username="admin",
        type="admin",
        is_superuser=1,
        is_staff=1,
    )
    user.set_password("123")
    user.save()
