from pprint import pprint
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from ...utilities.helpers import randomString, toJson
from ...models import Order, SoldTicket
from django.contrib.auth.decorators import permission_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.db import transaction


@permission_required("src.view_order")
def index(request):
    orders = Order.objects.order_by("-id").filter()
    return render(request, "cms/pages/order/index.html", {"orders": orders})


@permission_required("src.change_order")
def apply(request):
    if request.method == "POST":
        try:
            with transaction.atomic():
                order = Order.objects.filter(id=request.POST["id"]).first()

                if order.is_paid != 1:
                    for orderDetail in order.orderdetail_set.all():
                        for i in range(orderDetail.quantity):
                            soldTicket = SoldTicket()
                            soldTicket.code = createUniqueCode()
                            soldTicket.name = order.name
                            soldTicket.email = order.email
                            soldTicket.phone = order.phone
                            soldTicket.ticket_id = orderDetail.ticket_id
                            soldTicket.save()

                    order.is_paid = 1
                    order.save()

                html = render_to_string("email/orderSuccess.html", {"order": order})

                send_mail(
                    "Mua vé thành công",
                    "",
                    "nobmtpro2021@gmail.com",
                    [order.email],
                    fail_silently=False,
                    html_message=html,
                )

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

        return JsonResponse({"string": randomString(6)}, status=200)


def createUniqueCode():
    string = randomString(6)
    soldTicket = SoldTicket.objects.filter(code=string).first()
    if soldTicket:
        return createUniqueCode()
    return string
