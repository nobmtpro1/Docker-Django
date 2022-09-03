from django.urls import path
from ..views.cms import dashboard, ticket, account, order, admin,groupPermission

app_name = "cms"
urlpatterns = [
    path("auth/login", account.login, name="login"),
    path("logout", account.logout, name="logout"),
    path("", dashboard.index, name="dashboard"),
    # ticket
    path("ticket", ticket.index, name="ticket.index"),
    path("ticket/create", ticket.create, name="ticket.create"),
    path("ticket/update/<id>", ticket.update, name="ticket.update"),
    path("ticket/delete", ticket.delete, name="ticket.delete"),
    # order
    path("order", order.index, name="order.index"),
    path("order/apply", order.apply, name="order.apply"),
    # admin
    path("admin", admin.index, name="admin.index"),
    path("admin/create", admin.create, name="admin.create"),
    path("admin/update/<id>", admin.update, name="admin.update"),
    path("admin/delete", admin.delete, name="admin.delete"),
    # group permission
    path("group-permission", groupPermission.index, name="groupPermission.index"),
    path(
        "group-permission/create", groupPermission.create, name="groupPermission.create"
    ),
    path(
        "group-permission/update/<id>",
        groupPermission.update,
        name="groupPermission.update",
    ),
    path(
        "group-permission/delete", groupPermission.delete, name="groupPermission.delete"
    ),
]
