from django.urls import path
from ..views.cms import dashboard,ticket,account

app_name="cms"
urlpatterns = [
    path("auth/login", account.login, name="login"),
    path("logout", account.logout, name="logout"),
    path("", dashboard.index, name="dashboard"),
    path("ticket", ticket.index, name="ticket"),
]
