from django.core.management import BaseCommand
from catalog.models import Product, Category

class Command(BaseCommand):

    def handle(self, *args, **options):

        Product.objects.all().delete()

        product_list = [
            {'name_product': 'Молоко', 'description': 'ну молоко', 'category': 'Молочное', 'purchase_price': '50'},
            {'name_product': 'Сыр', 'description': 'ну сыр', 'category': 'Молочное', 'purchase_price': '100'},
            {'name_product': 'Хлеб', 'description': 'ну хлеб', 'category': 'Мучное', 'purchase_price': '15'},
            {'name_product': 'Булка', 'description': 'ну булка', 'category': 'Мучное', 'purchase_price': '30'},
            {'name_product': 'Рыба', 'description': 'ну не мясо', 'category': 'Рыба', 'purchase_price': '300'},

        ]
        product_for_create = []
        for product_item in product_list:
            product_for_create.append(Product(**product_item))

        Product.objects.bulk_create(product_for_create)
