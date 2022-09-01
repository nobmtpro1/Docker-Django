from django.urls import path
from ..views.web import home, livestream

app_name = "web"
urlpatterns = [
    path("", home.index, name="home"),
    path("get-cart", home.getCart, name="getCart"),
    path("checkout", home.checkout, name="checkout"),
    path("check-order-status", home.checkOrderStatus, name="checkOrderStatus"),
    path("thank-you", home.thankYou, name="thankYou"),
    path("livestream", livestream.index, name="livestream"),
]
