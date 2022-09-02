from pprint import pprint
from django.urls import resolve
from django.shortcuts import redirect
from django.contrib.auth import logout as auth_logout
import jwt

urlsLoginRequired = ["livestream"]

class AuthClient:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        appName = resolve(request.path_info).app_name
        urlName = resolve(request.path_info).url_name

        userClientToken = request.session.get("userClientToken", None)

        if userClientToken:
            payload = jwt.decode(userClientToken, "secret", algorithms=["HS256"])
            if payload:
                request.userClient = payload.get("user", None)

        if appName == "web" and urlName in urlsLoginRequired:

            if not userClientToken:
                return redirect("web:login")

            if not payload:
                return redirect("web:login")

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
