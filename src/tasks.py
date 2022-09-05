# Create your tasks here
from django.core.mail import send_mail
from django.template.loader import render_to_string
from celery import shared_task
from .utilities.helpers import randomString
from .models import UserClient

@shared_task
def add(x, y):
    print(x + y)
    return x + y


@shared_task
def printt(x):
    return x


@shared_task
def sendEmailOrderSuccess(order):
    html = render_to_string("email/orderSuccess.html", {"order": order})
    send_mail(
        "Mua vé thành công",
        "",
        "nobmtpro2021@gmail.com",
        [order["email"]],
        fail_silently=False,
        html_message=html,
    )

@shared_task
def testSchedule():
    user = UserClient.objects.filter(email="nobmtpro1@gmail.com").first()
    user.password = randomString(10)
    user.save()