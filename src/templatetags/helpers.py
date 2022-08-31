import datetime
from django import template

register = template.Library()


@register.simple_tag
def toInputDate(data):
    date = str(data)
    return date


@register.simple_tag
def toInputTime(data):
    date = str(data)
    d = datetime.datetime.strptime(date[:8], "%H:%M:%S")
    inputDate = d.strftime("%H:%M:%S")
    return inputDate
