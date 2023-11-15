from django.db import models

class Product(models.Model):
    name_product = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.CharField(max_length=200, verbose_name='Описание')
    image = models.ImageField(upload_to='image/', verbose_name='Изображение')
    category = models.CharField(max_length=100, verbose_name='Категория')
    purchase_price = models.IntegerField(verbose_name='Цена')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    last_modified_date = models.DateTimeField(auto_now=True,verbose_name='Дата последнего изменения')

class Category(models.Model):
    name_category = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.CharField(max_length=200, verbose_name='Описание')
    created_at = models.CharField(max_length=100, verbose_name='Создан')