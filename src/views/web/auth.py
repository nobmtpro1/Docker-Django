from pprint import pprint
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from ...models import UserClient
from marshmallow import Schema, fields, ValidationError, INCLUDE, validate
import bcrypt
from django.shortcuts import redirect


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
            request.session["loginError"] = list(err.messages.values())[0][0]
            request.session["loginDisplayed"] = False
            return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))

        user = UserClient.objects.get(email=request.POST["email"])

        if user and bcrypt.checkpw(
            request.POST["password"].encode("utf-8"), user.password.encode("utf-8")
        ):
            request.session["logged"] = True
            return redirect("web:home")
        else:
            request.session["loginError"] = "Fail"
            request.session["loginDisplayed"] = False
            return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))

    errorMessage = ""
    if request.session.get("loginDisplayed", True) == False:
        errorMessage = request.session["loginError"]
    request.session["loginDisplayed"] = True
    return render(request, "web/pages/login.html", {"errorMessage": errorMessage})


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
