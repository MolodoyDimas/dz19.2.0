from django.db import models
from users.models import User

class Product(models.Model):
    name_product = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.CharField(max_length=200, verbose_name='Описание')
    image = models.ImageField(upload_to='image/', verbose_name='Изображение', blank=True)
    category = models.CharField(max_length=100, verbose_name='Категория')
    purchase_price = models.IntegerField(verbose_name='Цена')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    last_modified_date = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE, verbose_name='Создал')
    publication = models.BooleanField(default=False, verbose_name="Опубликовано")


    def __str__(self):
        return f'{self.name_product}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name_product',)


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    version_number = models.IntegerField(verbose_name='Номер версии')
    version_name = models.TextField(max_length=100, verbose_name='Название версии')
    version_indication = models.BooleanField(default=True, verbose_name='Признак текущей версии')

    def __str__(self):
        return f'{self.version_name}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'


class Category(models.Model):
    name_category = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.CharField(max_length=200, verbose_name='Описание')

    def __str__(self):
        return f'{self.id, self.name_category}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
