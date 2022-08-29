from django.urls import path
from ..views.cms import dashboard

app_name="cms"
urlpatterns = [
    path("", dashboard.index, name="dashboard"),
]
