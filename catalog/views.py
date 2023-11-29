from django.shortcuts import render
from catalog.models import Product
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy


# class ProductCreateView(CreateView):
#     model = Product
#     fields = ('name_product', 'description', 'purchase_price', 'category')
#     success_url = reverse_lazy('catalog:index')

class ProductListView(ListView):
    model = Product

def contacts(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)
