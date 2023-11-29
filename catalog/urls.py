from django.urls import path
from catalog.views import ProductCreateView, ContactsCreateView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductCreateView.as_view(), name='index'),
    path('contacts/', ContactsCreateView.as_view(), name='contacts')
]