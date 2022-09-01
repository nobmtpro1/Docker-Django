from django.urls import path
from ..views.cms import dashboard,ticket,account,order

app_name="cms"
urlpatterns = [
    path("auth/login", account.login, name="login"),
    path("logout", account.logout, name="logout"),
    path("", dashboard.index, name="dashboard"),

    # ticket
    path("ticket", ticket.index, name="ticket.index"),
    path("ticket/create", ticket.create, name="ticket.create"),
    path("ticket/update/<id>", ticket.update, name="ticket.update"),
    path("ticket/delete", ticket.delete, name="ticket.delete"),

    # ticket
    path("order", order.index, name="order.index"),
    path("order/apply", order.apply, name="ticket.apply"),
]
