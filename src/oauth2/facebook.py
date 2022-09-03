import hashlib
import os
from pprint import pprint
import requests
from django.conf import settings


def facebookLoginUrl(request):
    state = hashlib.sha256(os.urandom(1024)).hexdigest()
    request.session["loginFacebookState"] = state
    redirectUri = settings.LOGIN_FACEBOOK_REDIRECT
    clientId = settings.LOGIN_FACEBOOK_CLIENT_ID

    return (
        "https://www.facebook.com/v14.0/dialog/oauth?"
        + "client_id="
        + clientId
        + "&redirect_uri="
        + redirectUri
        + "&state="
        + state
        + "&scope=email"
    )

def facebookLoginCallback(request):
    if request.GET["state"] != request.session["loginFacebookState"]:
        return False

    r = requests.get(
        "https://graph.facebook.com/v14.0/oauth/access_token?",
        params={
            "code": request.GET["code"],
            "client_id": settings.LOGIN_FACEBOOK_CLIENT_ID,
            "client_secret": settings.LOGIN_FACEBOOK_CLIENT_SECRET,
            "redirect_uri": settings.LOGIN_FACEBOOK_REDIRECT
        },
    )

    r.raise_for_status()
    res = requests.get(
        "https://graph.facebook.com/me?fields=name,email&access_token="
        + r.json()["access_token"]
    )
    res.raise_for_status()
    return res.json()