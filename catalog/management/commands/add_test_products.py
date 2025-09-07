from django.core.management.base import BaseCommand
from catalog.models import Category, Products

class Command(BaseCommand):
    help = 'Add test products to the database'

    def handle(self, *args, **kwargs):

        Category.objects.all().delete()
        Products.objects.all().delete()

        category, _ = Category.objects.get_or_create(name='Ягоды', description='.')

        products = [
            {'name': 'Брусника', 'category': category, 'price': 80},
            {'name': 'Малина', 'category': category, 'price': 30},
        ]

        for product in products:
            product, created = Products.objects.get_or_create(**product)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Book already exists: {product.name}'))
