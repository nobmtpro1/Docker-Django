from django.urls import path
from ..views.web import home,livestream

app_name="web"
urlpatterns = [
    path("", home.index, name="home"),
    path("get-cart", home.getCart, name="getCart"),
    path("livestream", livestream.index, name="livestream"),
]
