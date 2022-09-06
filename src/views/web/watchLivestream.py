import datetime
from pprint import pprint
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from ...utilities.helpers import toJson
from ...models import SoldTicket, Ticket


def index(request, slug, code):
    slugToList = slug.split("-")
    ticketId = slugToList[-1]

    ticket = Ticket.objects.filter(id=ticketId).first()
    if not ticket:
        return redirect("web:livestream")

    date = ticket.date
    time = ticket.time_from
    dateNow = datetime.date.today()
    timeNow = datetime.datetime.now().time()
    if date > dateNow or (date == dateNow and time > timeNow):
        return redirect("web:livestream")

    soldTicket = SoldTicket.objects.filter(code=code).first()
    if not soldTicket or soldTicket.ticket_id != ticket.id:
        return redirect("web:livestream")

    return render(request, "web/pages/watchLivestream.html", {"ticket": ticket})
