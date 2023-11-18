from django.urls import path
from catalog.views import index, contacts, product

urlpatterns = [
    path('', index, name =  'index'),
    path('contacts/', contacts, name ='contacts'),
    path('product/', product, name='product')
]