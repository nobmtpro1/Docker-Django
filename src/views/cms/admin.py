from pprint import pprint
from wsgiref.validate import validator
from django.http import JsonResponse
from django.shortcuts import render
from ...utilities.uploadFile import uploadFile, validateFile
from ...models import Ticket
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.models import Permission, Group, User
from marshmallow import Schema, fields, ValidationError, INCLUDE, validate

# validation
class AdminSchema(Schema):
    username = fields.String(required=True, validate=validate.Length(min=1, max=255))
    password = fields.String(required=True, validate=validate.Length(min=1, max=255))
    name = fields.String(required=True, validate=validate.Length(min=1, max=255))


def index(request):
    admins = User.objects.order_by("-id").filter(~Q(is_superuser=1))
    return render(request, "cms/pages/admin/index.html", {"admins": admins})


def create(request):
    if request.method == "POST":
        try:
            result = AdminSchema().load(request.POST, unknown=INCLUDE)
        except ValidationError as err:
            print(err.messages)
            return JsonResponse({"errors": err.messages}, status=400)

        if User.objects.filter(username=request.POST["username"]).first():
            return JsonResponse(
                {"errors": {"username": ["username has been taken"]}}, status=400
            )

        admin = User()
        admin.username = request.POST["username"]
        admin.first_name = request.POST["name"]
        admin.set_password(request.POST["password"])
        admin.save()

        for permission in request.POST["permissions"].split(","):
            p = Permission.objects.get(codename=permission)
            admin.user_permissions.add(p)

        for group in request.POST["groups"].split(","):
            g = Group.objects.get(id=group)
            admin.groups.add(g)

        return JsonResponse(request.POST, status=200)

    groups = Group.objects.all()
    permissions = Permission.objects.all()

    return render(
        request,
        "cms/pages/admin/create.html",
        {"permissions": permissions, "groups": groups},
    )


def update(request, id):
    if request.method == "POST":
        try:
            result = AdminSchema().load(
                request.POST, unknown=INCLUDE, partial=("password",)
            )
        except ValidationError as err:
            print(err.messages)
            return JsonResponse({"errors": err.messages}, status=400)

        admin = User.objects.filter(id=id).first()

        if request.POST["username"] != admin.username:
            if User.objects.filter(username=request.POST["username"]).first():
                return JsonResponse(
                    {"errors": {"username": ["username has been taken"]}}, status=400
                )

        admin.username = request.POST["username"]
        admin.first_name = request.POST["name"]
        if request.POST.get("password",None):
            admin.set_password(request.POST["password"])
        admin.save()

        admin.user_permissions.clear()
        for permission in request.POST["permissions"].split(","):
            p = Permission.objects.filter(codename=permission).first()
            admin.user_permissions.add(p)

        admin.groups.clear()
        for group in request.POST["groups"].split(","):
            g = Group.objects.filter(id=(group if group else 0)).first()
            admin.groups.add(g)

        return JsonResponse(request.POST, status=200)

    groups = Group.objects.all()
    permissions = Permission.objects.all()
    admin = User.objects.filter(id=id).first()
    groupIds = [group.id for group in admin.groups.all()]
    permissionIds = [permission.id for permission in admin.user_permissions.all()]

    return render(
        request,
        "cms/pages/admin/update.html",
        {
            "permissions": permissions,
            "groups": groups,
            "admin": admin,
            "groupIds": groupIds,
            "permissionIds": permissionIds,
        },
    )


def delete(request):
    if request.method == "POST":
        try:
            ticket = Ticket.objects.get(pk=request.POST["id"])
            ticket.delete()
            return JsonResponse(request.POST, status=200)
        except ValidationError as err:
            print(err.messages)
            return JsonResponse({"errors": err.messages}, status=400)
