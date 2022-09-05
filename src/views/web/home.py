from datetime import datetime, timedelta
from pprint import pprint
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, render

from ...tasks import add

from ...utilities.helpers import toJson
from ...models import Ticket, Order, OrderDetail
import json
from marshmallow import Schema, fields, ValidationError, INCLUDE, validate
from django.core import serializers


# validation
class CartSchema(Schema):
    name = fields.String(
        required=True,
        validate=validate.Length(min=1, max=255, error="Họ và tên không hợp lệ"),
        error_messages={
            "required": "Bạn chưa nhập họ và tên",
        },
    )
    phone = fields.String(
        required=True,
        validate=[
            validate.Regexp(
                r"^[-+]?[0-9]+$",
                error="Số điện thoại không hợp lệ",
            ),
            validate.Length(
                min=10,
                max=11,
                error="Số điện thoại phải chứa 10 đến 11 số",
            ),
        ],
        error_messages={
            "required": "Bạn chưa nhập số điện thoại",
            "invalid": "Số điện thoại không hợp lệ",
        },
    )
    email = fields.Email(
        required=True,
        validate=validate.Length(min=1, max=255, error="Email không hợp lệ"),
        error_messages={
            "required": "Bạn chưa nhập email",
            "invalid": "Email không hợp lệ",
        },
    )


def index(request):
    tickets = Ticket.objects.order_by("-id").filter()

    return render(
        request,
        "web/pages/home.html",
        {"tickets": tickets, "types": ["online", "offline"]},
    )


def getCart(request):
    if request.method == "POST":
        return JsonResponse({"cart": _calculateCart(request)}, status=200)


def checkout(request):
    if request.method == "POST":
        try:
            result = CartSchema().load(request.POST, unknown=INCLUDE)
        except ValidationError as err:
            print(err.messages)
            return JsonResponse({"errors": err.messages}, status=400)

        cart = _calculateCart(request)

        if cart["totalQuantity"] == 0:
            return JsonResponse(
                {"errors": {"Giỏ hàng": ["Bạn chưa nhập số lượng sản phẩm"]}},
                status=400,
            )

        order = Order()
        order.name = request.POST["name"]
        order.email = request.POST["email"]
        order.phone = request.POST["phone"]
        order.payment = "transfer"
        order.total = cart["total"]
        order.save()

        for item in cart["items"]:
            orderDetail = OrderDetail()
            orderDetail.order_id = order.id
            orderDetail.ticket_id = int(item["id"])
            orderDetail.quantity = int(item["quantity"])
            orderDetail.data = item["data"]
            orderDetail.save()

        return JsonResponse(
            {
                "cart": cart,
                "order": json.loads(
                    serializers.serialize(
                        "json",
                        [
                            order,
                        ],
                    )
                ),
            },
            status=200,
        )


def checkOrderStatus(request):
    if request.method == "POST":
        order = Order.objects.get(pk=request.POST["orderId"])
        if order.is_paid == 1:
            return JsonResponse({"is_paid": 1}, status=200)
        else:
            return JsonResponse({"errors": {"error": ["fail"]}}, status=400)


def thankYou(request):
    return render(
        request,
        "web/pages/thankYou.html",
        {},
    )


def _calculateCart(request):
    cart = {"total": 0, "totalQuantity": 0, "items": []}

    requestCart = json.loads(request.POST["cart"])

    for item in requestCart:
        if int(item["quantity"]) > 0:
            ticket = Ticket.objects.get(pk=int(item["id"]))
            item["data"] = serializers.serialize(
                "json",
                [
                    ticket,
                ],
            )
            cart["total"] += ticket.price * int(item["quantity"])
            cart["totalQuantity"] += int(item["quantity"])
            cart["items"].append(item)

    return cart
