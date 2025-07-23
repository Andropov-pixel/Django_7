from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'заполнения базы-данных о продуктах'

    def handle(self, *args, **kwargs):
        # Удаляем существующие записи
        Product.objects.all().delete()

        сategory, _ = Category.objects.get_or_create(name='Фрукты')

        products = [
            {'name': 'апельсин',"description": "оранжевый", 'сategory': сategory},
            {"name": "яблоко", "description": "зеленое", 'сategory': сategory}
        ]

        for prod in products:
            product, created = Product.objects.get_or_create(**prod)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added student: '
                                                     f'{product.name} {product.description}'))
            else:
                self.stdout.write(self.style.WARNING(f'Student already exists: '
                                                     f'{product.name} {product.description}'))