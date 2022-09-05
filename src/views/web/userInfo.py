from pprint import pprint
from django.http import HttpResponse
from django.shortcuts import render


def index(request,email):
    return render(request, "web/pages/userInfo.html", {})
