import hashlib
import os
from pprint import pprint
import requests
from django.conf import settings


def googleLoginUrl(request):
    state = hashlib.sha256(os.urandom(1024)).hexdigest()
    request.session["loginGoogleState"] = state
    scope = "https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email"
    redirectUri = settings.LOGIN_GOOGLE_REDIRECT
    clientId = settings.LOGIN_GOOGLE_CLIENT_ID
    return (
        "https://accounts.google.com/o/oauth2/v2/auth?"
        + "scope="
        + scope
        + "&"
        + "access_type=offline&"
        + "include_granted_scopes=true&"
        + "response_type=code&"
        + "state="
        + state
        + "&"
        + "redirect_uri="
        + redirectUri
        + "&"
        + "client_id="
        + clientId
    )


def googleLoginCallback(request):
    if request.GET["state"] != request.session["loginGoogleState"]:
        return False

    r = requests.post(
        "https://oauth2.googleapis.com/token",
        headers={"content-type": "application/x-www-form-urlencoded"},
        params={
            "code": request.GET["code"],
            "client_id": settings.LOGIN_GOOGLE_CLIENT_ID,
            "client_secret": settings.LOGIN_GOOGLE_CLIENT_SECRET,
            "redirect_uri": settings.LOGIN_GOOGLE_REDIRECT,
            "grant_type": "authorization_code",
        },
    )

    r.raise_for_status()
    res = requests.get(
        "https://www.googleapis.com/oauth2/v3/userinfo?access_token="
        + r.json()["access_token"]
    )
    res.raise_for_status()
    return res.json()
