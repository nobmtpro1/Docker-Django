from pprint import pprint
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    pprint(request.userClient)
    return render(request, "web/pages/livestream.html", {})
