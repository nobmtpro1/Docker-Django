from http.client import HTTPResponse
from django.urls import resolve

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        urlName = resolve(request.path_info).url_name
        if urlName == "post":
            request.abc ="abc post"
        else:
            request.abc ="abc home"
        
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
