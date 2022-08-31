from pprint import pprint
from wsgiref.validate import validator
from django.http import JsonResponse
from django.shortcuts import render
from ...utilities.uploadFile import uploadFile, validateFile
from ...models import Ticket
from marshmallow import Schema, fields, ValidationError, INCLUDE, validate


# validation
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
    tickets = Ticket.objects.order_by("-id")
    return render(request, "cms/pages/ticket/index.html", {"tickets": tickets})


def create(request):
    if request.method == "POST":
        try:
            result = TicketSchema().load(request.POST, unknown=INCLUDE)
        except ValidationError as err:
            print(err.messages)
            return JsonResponse({"errors": err.messages}, status=400)

        if "image" in request.FILES:
            return JsonResponse({"errors": {"image": ["File is required"]}}, status=400)
        error = validateFile(request.FILES["image"], "image", 10000000)
        if error:
            return JsonResponse({"errors": {"image": [error]}}, status=400)

        ticket = Ticket()
        ticket.type = "online" if request.POST["type"] == "online" else "offline"
        ticket.name = request.POST["name"]
        ticket.price = request.POST["price"]
        ticket.date = request.POST["date"]
        ticket._from = request.POST["_from"]
        ticket.to = request.POST["to"]
        ticket.quantity = request.POST["quantity"]
        ticket.address = request.POST["address"]
        ticket.link_video = request.POST["link_video"]
        ticket.image = uploadFile(request.FILES["image"], "/static/uploads/images/")
        ticket.save()

        return JsonResponse(request.POST, status=200)

    return render(request, "cms/pages/ticket/create.html", {})


def update(request, id):
    if request.method == "POST":
        try:
            result = TicketSchema().load(request.POST, unknown=INCLUDE)
        except ValidationError as err:
            print(err.messages)
            return JsonResponse({"errors": err.messages}, status=400)

        if "image" in request.FILES:
            error = validateFile(request.FILES["image"], "image", 10000000)
            if error:
                return JsonResponse({"errors": {"image": [error]}}, status=400)

        ticket = Ticket.objects.get(pk=id)
        ticket.type = "online" if request.POST["type"] == "online" else "offline"
        ticket.name = request.POST["name"]
        ticket.price = request.POST["price"]
        ticket.date = request.POST["date"]
        ticket._from = request.POST["_from"]
        ticket.to = request.POST["to"]
        ticket.quantity = request.POST["quantity"]
        ticket.address = request.POST["address"]
        ticket.link_video = request.POST["link_video"]
        if "image" in request.FILES:
            ticket.image = uploadFile(request.FILES["image"], "/static/uploads/images/")
        ticket.save()
        pprint(request.POST["date"])
        return JsonResponse(request.POST, status=200)

    ticket = Ticket.objects.get(pk=id)
    ticket.from_ = ticket._from
    return render(request, "cms/pages/ticket/update.html", {"ticket": ticket})


def delete(request):
    if request.method == "POST":
        try:
            ticket = Ticket.objects.get(pk=request.POST["id"])
            ticket.delete()
            return JsonResponse(request.POST, status=200) 
        except ValidationError as err:
            print(err.messages)
            return JsonResponse({"errors": err.messages}, status=400)
