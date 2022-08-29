from django import template

register = template.Library()


@register.inclusion_tag("cms/partials/sidebar.html")
def sidebar(request):
    return {"request": request}
