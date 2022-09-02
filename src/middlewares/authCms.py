from django.urls import resolve
from django.shortcuts import redirect
from django.contrib.auth import logout as auth_logout


class AuthCms:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        appName = resolve(request.path_info).app_name

        if appName == "cms" and resolve(request.path_info).url_name not in ["login"]:
            if not request.user.is_authenticated:
                return redirect("cms:login")

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
