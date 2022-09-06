from pprint import pprint
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from ...utilities.helpers import toJson
from ...models import SoldTicket
from django.template.defaultfilters import slugify
import datetime


def index(request):
    if request.method == "POST":
        soldTicket = SoldTicket.objects.filter(code=request.POST["code"]).first()

        if not soldTicket:
            return JsonResponse({"error": "Code không tồn tại"}, status=400)

        date = soldTicket.ticket.date
        time = soldTicket.ticket.time_from
        dateNow = datetime.date.today()
        timeNow = datetime.datetime.now().time()

        if date > dateNow:
            return JsonResponse({"error": "Chưa đến ngày livestream"}, status=400)

        if date == dateNow and time > timeNow:
            return JsonResponse({"error": "Chưa đến giờ livestream"}, status=400)

        return JsonResponse(
            {
                "url": reverse(
                    "web:watchLivestream",
                    kwargs={
                        "slug": slugify(
                            soldTicket.ticket.name + " " + str(soldTicket.ticket_id)
                        ),
                        "code": soldTicket.code,
                    },
                )
            },
            status=200,
        )
    return render(request, "web/pages/livestream.html", {})
