# Generated by Django 4.2.7 on 2023-12-05 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(max_length=100, verbose_name='Наименование')),
                ('description', models.CharField(max_length=200, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_product', models.CharField(max_length=100, verbose_name='Наименование')),
                ('description', models.CharField(max_length=200, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, upload_to='image/', verbose_name='Изображение')),
                ('category', models.CharField(max_length=100, verbose_name='Категория')),
                ('purchase_price', models.IntegerField(verbose_name='Цена')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('last_modified_date', models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Создал')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ('name_product',),
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_number', models.IntegerField(verbose_name='Номер версии')),
                ('version_name', models.TextField(max_length=100, verbose_name='Название версии')),
                ('version_indication', models.BooleanField(default=True, verbose_name='Признак текущей версии')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Версия',
                'verbose_name_plural': 'Версии',
            },
        ),
    ]
