import datetime
import locale
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


@register.simple_tag
def formatDatetime(date, fromFormat, toFormat):
    date = str(date)
    date = datetime.datetime.strptime(date, fromFormat)
    date = date.strftime(toFormat)
    return date


@register.filter(name="subtract")
def subtract(value, arg):
    return value - arg


@register.filter
def formatThousandsNumber(value, type):
    return "{0:,}".format(value).replace(",", type)


@register.filter
def getByKey(data, key):
    return data.get(key, "")


@register.filter
def getByIndex(data, index):
    return data[index]

