from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required



def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if (user is not None):
            auth_login(request, user)
            return redirect("cms:dashboard")
        else:
            return redirect(request.META.get("HTTP_REFERER"))
    if request.user.is_authenticated:
        return redirect("cms:dashboard")
    return render(request, "cms/pages/account/login.html", {})


def logout(request):
    auth_logout(request)
    return redirect("cms:login")