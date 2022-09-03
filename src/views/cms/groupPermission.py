from pprint import pprint
from tokenize import group
from wsgiref.validate import validator
from django.http import JsonResponse
from django.shortcuts import render
from ...models import Ticket
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.models import Permission, Group
from marshmallow import Schema, fields, ValidationError, INCLUDE, validate


# validation
class GroupSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=1, max=255))


def index(request):
    groups = Group.objects.order_by("-id").filter()
    return render(request, "cms/pages/group/index.html", {"groups": groups})


def create(request):
    if request.method == "POST":
        try:
            result = GroupSchema().load(request.POST, unknown=INCLUDE)
        except ValidationError as err:
            print(err.messages)
            return JsonResponse({"errors": err.messages}, status=400)

        group = Group()
        group.name = request.POST["name"]
        group.save()

        for permission in request.POST["permissions"].split(","):
            p = Permission.objects.get(codename=permission)
            group.permissions.add(p)

        return JsonResponse(request.POST, status=200)

    permissions = Permission.objects.all()
    return render(request, "cms/pages/group/create.html", {"permissions": permissions})


def update(request, id):
    if request.method == "POST":
        try:
            result = GroupSchema().load(request.POST, unknown=INCLUDE)
        except ValidationError as err:
            print(err.messages)
            return JsonResponse({"errors": err.messages}, status=400)

        group = Group.objects.filter(id=id).first()
        group.name = request.POST["name"]
        group.save()

        group.permissions.clear()
        for permission in request.POST["permissions"].split(","):
            p = Permission.objects.get(codename=permission)
            group.permissions.add(p)

        return JsonResponse(request.POST, status=200)

    permissions = Permission.objects.all()
    group = Group.objects.filter(id=id).first()
    permissionIds = [i.id for i in group.permissions.all()]

    pprint(permissionIds)
    return render(
        request,
        "cms/pages/group/update.html",
        {"permissions": permissions, "group": group, "permissionIds": permissionIds},
    )


def delete(request):
    if request.method == "POST":
        try:
            group = Group.objects.filter(id=request.POST["id"]).first()
            group.permissions.clear()
            group.delete()
            return JsonResponse(request.POST, status=200)
        except:
            return JsonResponse({"errors": "fail"}, status=400)
