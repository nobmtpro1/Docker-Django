from pprint import pprint
from wsgiref.validate import validator
from django.http import JsonResponse
from django.shortcuts import render
from ...utilities.uploadFile import uploadFile, validateFile
from ...models import Ticket
from marshmallow import Schema, fields, ValidationError, INCLUDE, validate


class TicketSchema(Schema):
    type = fields.String(required=True, validate=validate.Length(min=1, max=255))
    name = fields.String(required=True, validate=validate.Length(min=1, max=255))
    date = fields.String(required=True, validate=validate.Length(min=1, max=255))
    _from = fields.String(required=True, validate=validate.Length(min=1, max=255))
    to = fields.String(required=True, validate=validate.Length(min=1, max=255))
    quantity = fields.Integer(
        required=True, validate=validate.Range(min=1, max=10**11 - 1)
    )
    address = fields.String(required=True, validate=validate.Length(min=1, max=255))
    price = fields.Integer(
        required=True, validate=validate.Range(min=1, max=10**20 - 1)
    )
    link_video = fields.String(required=True, validate=validate.Length(min=1, max=255))


def index(request):
    return render(request, "cms/pages/ticket/index.html", {})


def create(request):
    if request.method == "POST":
        try:
            result = TicketSchema().load(request.POST, unknown=INCLUDE)
        except ValidationError as err:
            print(err.messages)
            return JsonResponse({"errors": err.messages}, status=400)

        error = validateFile(request.FILES["image"], "image", 10000000)
        if error:
            return JsonResponse({"errors": {"image": [error]}}, status=400)

        record = Ticket(
            type="online" if request.POST["type"] == "online" else "offline",
            name=request.POST["name"],
            price=request.POST["price"],
            date=request.POST["date"],
            _from=request.POST["_from"],
            to=request.POST["to"],
            quantity=request.POST["quantity"],
            address=request.POST["address"],
            link_video=request.POST["link_video"],
            image=uploadFile(request.FILES["image"], "/static/uploads/images/"),
        )
        record.save()

        return JsonResponse(request.POST, status=200)

    return render(request, "cms/pages/ticket/create.html", {})


def update(request):
    return render(request, "cms/pages/ticket/index.html", {})


def delete(request):
    return render(request, "cms/pages/ticket/index.html", {})
