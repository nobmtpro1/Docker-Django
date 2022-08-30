from django.urls import path
from ..views.web import home,post

app_name="web"
urlpatterns = [
    path("", home.index, name="home"),
    path("post", post.index, name="post"),
]
