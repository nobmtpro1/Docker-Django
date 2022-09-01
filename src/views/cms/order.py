from pprint import pprint
from wsgiref.validate import validator
from django.http import JsonResponse
from django.shortcuts import render
from ...utilities.uploadFile import uploadFile, validateFile
from ...models import Order


def index(request):
    orders = Order.objects.order_by("-id")
    return render(request, "cms/pages/ticket/index.html", {"orders": orders})


def apply(request):
    if request.method == "POST":
        try:
            # ticket = Ticket.objects.get(pk=request.POST["id"])
            # ticket.delete()
            return JsonResponse(request.POST, status=200)
        except:
            return JsonResponse({"errors": "Fail"}, status=400)
