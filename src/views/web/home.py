from pprint import pprint
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from ...models import Ticket


def index(request):
    tickets = Ticket.objects.order_by("-id")
    return render(
        request,
        "web/pages/home.html",
        {"tickets": tickets, "types": ["online", "offline"]},
    )


def getCart(request):
    return JsonResponse({"abc":123}, status=200)
