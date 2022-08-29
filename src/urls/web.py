from django.urls import path
from ..views.web import home,post

urlpatterns = [
    path("", home.index, name="home"),
    path("post", post.index, name="post"),
]
