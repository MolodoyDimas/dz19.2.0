from django.shortcuts import render
from catalog.models import Product


def index(request):
    product_list = Product.objects.all()
    context = {
        'product_list': product_list,
        'title': 'Главная'
    }
    return render(request, 'catalog/index.html', context)


def contacts(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)
