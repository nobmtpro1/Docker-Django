from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "cms/pages/ticket/index.html", {})
