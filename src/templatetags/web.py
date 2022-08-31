from django import template

register = template.Library()


@register.inclusion_tag("web/partials/header.html")
def header(request):
    return {"request": request}


@register.inclusion_tag("web/partials/footer.html")
def footer(request):
    return {"request": request}


@register.inclusion_tag("web/partials/popup.html")
def popup(request):
    return {"request": request}
