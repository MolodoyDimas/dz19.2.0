from django import template

register = template.Library()

@register.filter()
def mymedia(x):
    if x:
        return f'/media/{str(x)}'
    return
