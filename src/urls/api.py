from django.urls import path
from ..views.api import session

app_name = "api"
urlpatterns = [
    path("session", session.index, name="session"),
]
