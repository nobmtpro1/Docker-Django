from pprint import pprint
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from ...oauth2.facebook import facebookLoginUrl,facebookLoginCallback

from ...oauth2.google import googleLoginCallback, googleLoginUrl

from ...utilities.helpers import getFlashSession, setFlashSession
from ...models import UserClient
from marshmallow import Schema, fields, ValidationError, INCLUDE, validate
import bcrypt
from django.shortcuts import redirect
import jwt
import json
from django.core import serializers


# validation
class RegisterSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=5, max=255))
    email = fields.Email(required=True, validate=validate.Length(min=5, max=255))
    password = fields.String(required=True, validate=validate.Length(min=5, max=255))


def login(request):
    if request.method == "POST":
        try:
            result = RegisterSchema().load(
                request.POST, unknown=INCLUDE, partial=("name",)
            )
        except ValidationError as err:
            print(err.messages)
            setFlashSession(request, "loginError", list(err.messages.values())[0][0])
            return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))

        user = UserClient.objects.filter(email=request.POST["email"]).first()

        if user and bcrypt.checkpw(
            request.POST["password"].encode("utf-8"), user.password.encode("utf-8")
        ):
            request.session["userClientToken"] = jwt.encode(
                {"userId": user.id},
                "secret",
                algorithm="HS256",
            )
            return redirect("web:home")
        else:
            setFlashSession(
                request, "loginError", "Tài khoản hoặc mật khẩu không chính xác"
            )
            return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))

    googleLoginLink = googleLoginUrl(request)
    facebookLoginLink = facebookLoginUrl(request)
    errorMessage = getFlashSession(request, "loginError")
    return render(
        request,
        "web/pages/login.html",
        {
            "errorMessage": errorMessage,
            "googleLoginLink": googleLoginLink,
            "facebookLoginLink": facebookLoginLink,
        },
    )


def register(request):
    if request.method == "POST":
        try:
            result = RegisterSchema().load(request.POST, unknown=INCLUDE)
        except ValidationError as err:
            print(err.messages)
            return JsonResponse({"errors": err.messages}, status=400)

        user = UserClient.objects.filter(email=request.POST["email"])

        if user:
            return JsonResponse(
                {"errors": {"user": ["Email has been taken"]}}, status=400
            )

        user = UserClient()
        user.name = request.POST["name"]
        user.email = request.POST["email"]
        user.password = bcrypt.hashpw(
            request.POST["password"].encode("utf-8"), bcrypt.gensalt()
        ).decode("utf-8")
        user.save()

        return JsonResponse({}, status=200)

    return render(request, "web/pages/register.html", {})


def logout(request):
    request.session["userClientToken"] = None
    return redirect(request.GET.get("next", ""))


def loginSocialCallback(request, provider):
    # return JsonResponse(request.GET)
    socialUser = None
    name = None
    email = None
    if provider == "google":
        socialUser = googleLoginCallback(request)
        name = socialUser["name"]
        email = socialUser["email"]

    if provider == "facebook":
        socialUser = facebookLoginCallback(request)
        pprint(socialUser)
        name = socialUser["name"]
        email = socialUser["email"]

    if socialUser:
        user = UserClient.objects.filter(email=email).first()
        if not user:
            user = UserClient()
            user.name = name
            user.email = email
            user.save()
        request.session["userClientToken"] = jwt.encode(
            {"userId": user.id},
            "secret",
            algorithm="HS256",
        )

    return redirect("web:home")
