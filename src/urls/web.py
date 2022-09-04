from django.urls import path
from ..views.web import home, livestream, auth

app_name = "web"
urlpatterns = [
    path("", home.index, name="home"),
    path("get-cart", home.getCart, name="getCart"),
    path("checkout", home.checkout, name="checkout"),
    path("check-order-status", home.checkOrderStatus, name="checkOrderStatus"),
    path("thank-you", home.thankYou, name="thankYou"),
    path("livestream", livestream.index, name="livestream"),
    path("login", auth.login, name="login"),
    path("logout", auth.logout, name="logout"),
    path("register", auth.register, name="register"),
    path("oauth2/<provider>/callback", auth.loginSocialCallback, name="loginSocailCallback"),

    path("redis", home.redis, name="redis"),
]
