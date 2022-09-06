from pprint import pprint
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.db.models import Prefetch
from ...utilities.helpers import toJson
from ...models import UserClient, SoldTicket, Ticket


def index(request, email):
    user = UserClient.objects.filter(email=email).first()
    soldTickets = SoldTicket.objects.filter(email=email).prefetch_related("ticket")

    return render(
        request, "web/pages/userInfo.html", {"user": user, "soldTickets": soldTickets}
    )
