from django.db import models


class Product(models.Model):
    name_product = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.CharField(max_length=200, verbose_name='Описание')
    image = models.ImageField(upload_to='image/', verbose_name='Изображение', blank=True)
    category = models.CharField(max_length=100, verbose_name='Категория')
    purchase_price = models.IntegerField(verbose_name='Цена')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    last_modified_date = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.id} {self.name_product} {self.purchase_price} {self.category}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name_product',)


class Category(models.Model):
    name_category = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.CharField(max_length=200, verbose_name='Описание')

    def __str__(self):
        return f'{self.id, self.name_category}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
