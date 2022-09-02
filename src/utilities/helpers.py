def setFlashSession(request, key, value):
    request.session[key] = value


def getFlashSession(request, key):
    value = request.session.get(key, False)
    if value:
        request.session[key] = None
        return value

    return None
