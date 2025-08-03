from django.core.management.base import BaseCommand
from products.models import Category, Product
from django.utils.text import slugify


class Command(BaseCommand):
    help = 'Populate the database with sample products'

    def handle(self, *args, **options):
        # Create categories
        categories_data = [
            {'name': 'Electronics', 'description': 'Latest electronic gadgets and accessories'},
            {'name': 'Clothing', 'description': 'Fashion and apparel for all occasions'},
            {'name': 'Books', 'description': 'Books across various genres and subjects'},
            {'name': 'Home & Garden', 'description': 'Everything for your home and garden'},
            {'name': 'Sports & Fitness', 'description': 'Sports equipment and fitness gear'},
        ]

        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={
                    'slug': slugify(cat_data['name']),
                    'description': cat_data['description']
                }
            )
            if created:
                self.stdout.write(f'Created category: {category.name}')

        # Create products
        products_data = [
            # Electronics
            {
                'name': 'Wireless Bluetooth Headphones',
                'category': 'Electronics',
                'description': 'High-quality wireless headphones with noise cancellation and 30-hour battery life.',
                'price': 149.99,
                'stock': 25
            },
            {
                'name': 'Smartphone Case',
                'category': 'Electronics',
                'description': 'Durable protective case for smartphones with shock-absorbing technology.',
                'price': 29.99,
                'stock': 50
            },
            {
                'name': 'Laptop Stand',
                'category': 'Electronics',
                'description': 'Adjustable aluminum laptop stand for ergonomic workspace setup.',
                'price': 79.99,
                'stock': 15
            },
            
            # Clothing
            {
                'name': 'Cotton T-Shirt',
                'category': 'Clothing',
                'description': 'Comfortable 100% cotton t-shirt available in multiple colors and sizes.',
                'price': 24.99,
                'stock': 100
            },
            {
                'name': 'Denim Jeans',
                'category': 'Clothing',
                'description': 'Classic straight-fit denim jeans made from premium cotton blend.',
                'price': 89.99,
                'stock': 40
            },
            {
                'name': 'Winter Jacket',
                'category': 'Clothing',
                'description': 'Warm and waterproof winter jacket with insulated lining.',
                'price': 159.99,
                'stock': 20
            },
            
            # Books
            {
                'name': 'Python Programming Guide',
                'category': 'Books',
                'description': 'Comprehensive guide to Python programming for beginners and experts.',
                'price': 39.99,
                'stock': 30
            },
            {
                'name': 'Mystery Novel Collection',
                'category': 'Books',
                'description': 'A collection of bestselling mystery novels by renowned authors.',
                'price': 19.99,
                'stock': 45
            },
            
            # Home & Garden
            {
                'name': 'Indoor Plant Pot Set',
                'category': 'Home & Garden',
                'description': 'Set of 3 ceramic plant pots with drainage holes, perfect for indoor plants.',
                'price': 34.99,
                'stock': 35
            },
            {
                'name': 'LED Desk Lamp',
                'category': 'Home & Garden',
                'description': 'Modern LED desk lamp with adjustable brightness and USB charging port.',
                'price': 49.99,
                'stock': 25
            },
            
            # Sports & Fitness
            {
                'name': 'Yoga Mat',
                'category': 'Sports & Fitness',
                'description': 'Non-slip yoga mat with extra cushioning for comfort during practice.',
                'price': 59.99,
                'stock': 40
            },
            {
                'name': 'Water Bottle',
                'category': 'Sports & Fitness',
                'description': 'Stainless steel water bottle with insulation to keep drinks cold for 24 hours.',
                'price': 27.99,
                'stock': 60
            },
        ]

        for product_data in products_data:
            category = Category.objects.get(name=product_data['category'])
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults={
                    'slug': slugify(product_data['name']),
                    'category': category,
                    'description': product_data['description'],
                    'price': product_data['price'],
                    'stock': product_data['stock'],
                    'available': True
                }
            )
            if created:
                self.stdout.write(f'Created product: {product.name}')

        self.stdout.write(
            self.style.SUCCESS('Successfully populated the database with sample data!')
        )
