from django import template
from django.conf import settings

register = template.Library()

@register.filter()
def mymedia(x):
    if x:
        return f'/media/{str(x)}'
    return

def mediapath(file_name):
    if file_name:
        return f'{settings.MEDIA_URL}{file_name}'
    return ''
# тег <img src="{% mediapath object.image %}" />
# Но я незнаю куда нужно его запихать, т.к картинки работают через фильтр, или я что-то не понял