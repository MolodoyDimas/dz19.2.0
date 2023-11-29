from django.shortcuts import render
from catalog.models import Product
from django.views.generic import CreateView
from django.urls import reverse_lazy

# def index(request):
#     product_list = Product.objects.all()
#     context = {
#         'product_list': product_list,
#         'title': 'Главная'
#     }
#     return render(request, 'catalog/index.html', context)

class ProductCreateView(CreateView):
    model = Product
    fields = ('name_product', 'description', 'purchase_price', 'category')
    success_url = reverse_lazy('catalog:list')

class ContactsCreateView(CreateView):
    model = Product


# def contacts(request):
#     context = {
#         'title': 'Контакты'
#     }
#     return render(request, 'catalog/contacts.html', context)
