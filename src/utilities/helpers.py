import json
import random
import string
from django.core import serializers


def setFlashSession(request, key, value):
    request.session[key] = value


def getFlashSession(request, key):
    value = request.session.get(key, False)
    if value:
        request.session[key] = None
        return value

    return None


def toJson(instance, type="list"):

    if type == "obj":
        return json.dumps(
            json.loads(
                serializers.serialize(
                    "json",
                    [instance],
                )
            )[0],
            indent=4,
        )

    return serializers.serialize(
        "json",
        instance,
    )


def randomString(length):
    characters = string.ascii_lowercase + string.digits
    return "".join(random.choice(characters) for i in range(length))
