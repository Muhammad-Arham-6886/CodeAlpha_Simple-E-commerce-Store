from django.core.management.base import BaseCommand
from products.models import Product
from django.utils.text import slugify


class Command(BaseCommand):
    help = 'Update products with detailed descriptions and image URLs'

    def handle(self, *args, **options):
        products_data = [
            {
                'name': 'Wireless Bluetooth Headphones',
                'description': '''Experience premium audio quality with these state-of-the-art wireless Bluetooth headphones. 
                
Features:
• Active Noise Cancellation (ANC) technology
• 30-hour battery life with quick charge
• Hi-Res Audio certified drivers
• Comfortable over-ear design with memory foam
• Touch controls for easy operation
• Built-in microphone for hands-free calls
• Compatible with all Bluetooth devices
• Foldable design for travel convenience

Perfect for music lovers, professionals, and travelers who demand the best audio experience.''',
                'image_url': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400&h=300&fit=crop'
            },
            {
                'name': 'Smartphone Case',
                'description': '''Protect your valuable smartphone with this premium protective case featuring military-grade protection.

Features:
• Drop protection up to 10 feet
• Shock-absorbing TPU corners
• Scratch-resistant back panel
• Precise cutouts for all ports and buttons
• Wireless charging compatible
• Raised edges protect camera and screen
• Easy grip texture prevents slipping
• Available in multiple colors

Designed for maximum protection without compromising style or functionality.''',
                'image_url': 'https://images.unsplash.com/photo-1556656793-08538906a9f8?w=400&h=300&fit=crop'
            },
            {
                'name': 'Laptop Stand',
                'description': '''Ergonomic aluminum laptop stand designed to improve your workspace comfort and productivity.

Features:
• Adjustable height and angle (0-60°)
• Premium aluminum construction
• Heat dissipation design keeps laptop cool
• Non-slip silicone pads protect your device
• Foldable and portable design
• Compatible with laptops 10-17 inches
• Cable management system
• Sturdy construction holds up to 22 lbs

Transform any space into a comfortable and efficient workspace.''',
                'image_url': 'https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=400&h=300&fit=crop'
            },
            {
                'name': 'Cotton T-Shirt',
                'description': '''Ultra-soft premium cotton t-shirt that combines comfort, style, and durability.

Features:
• 100% organic cotton fabric
• Pre-shrunk for lasting fit
• Reinforced stitching at stress points
• Tagless label for comfort
• Available in multiple sizes (XS-3XL)
• Machine washable and colorfast
• Classic fit that's not too loose or tight
• Breathable fabric perfect for all seasons

Essential wardrobe staple that goes with everything. Perfect for casual wear or layering.''',
                'image_url': 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400&h=300&fit=crop'
            },
            {
                'name': 'Denim Jeans',
                'description': '''Classic straight-fit denim jeans crafted from premium cotton blend for ultimate comfort and style.

Features:
• Premium stretch denim (98% cotton, 2% elastane)
• Classic 5-pocket design
• YKK zipper and metal hardware
• Reinforced stress points
• Traditional straight-leg fit
• Machine washable
• Fade-resistant color treatment
• Available in multiple washes and sizes

Timeless design that never goes out of style. Perfect for casual and smart-casual occasions.''',
                'image_url': 'https://images.unsplash.com/photo-1542272604-787c3835535d?w=400&h=300&fit=crop'
            },
            {
                'name': 'Winter Jacket',
                'description': '''Stay warm and stylish with this premium winter jacket featuring advanced insulation technology.

Features:
• Water-resistant outer shell
• 650-fill down insulation
• Adjustable hood with faux fur trim
• Multiple pockets with secure zippers
• Elastic cuffs and adjustable hem
• Reflective details for visibility
• Machine washable down-alternative fill
• Temperature rating: -10°F to 50°F

Perfect protection against harsh weather conditions while maintaining a fashionable appearance.''',
                'image_url': 'https://images.unsplash.com/photo-1551028719-00167b16eac5?w=400&h=300&fit=crop'
            },
            {
                'name': 'Python Programming Guide',
                'description': '''Comprehensive Python programming guide for beginners to advanced developers.

What's Inside:
• 800+ pages of expert content
• Step-by-step tutorials and examples
• Real-world projects and case studies
• Best practices and coding standards
• Data structures and algorithms
• Web development with Django/Flask
• Data science and machine learning basics
• Interview preparation questions

Written by industry experts with 15+ years of experience. Includes access to online resources and code repository.''',
                'image_url': 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=400&h=300&fit=crop'
            },
            {
                'name': 'Mystery Novel Collection',
                'description': '''Thrilling collection of bestselling mystery novels from renowned authors around the world.

Collection Includes:
• 5 award-winning mystery novels
• Stories from different cultures and settings
• Complex plots with unexpected twists
• Well-developed characters and dialogue
• Various sub-genres: cozy, noir, psychological
• Authors include bestselling and emerging writers
• Perfect binding with high-quality paper
• Collectible dust jackets

Hours of entertainment for mystery lovers and those seeking engaging storytelling.''',
                'image_url': 'https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=400&h=300&fit=crop'
            },
            {
                'name': 'Indoor Plant Pot Set',
                'description': '''Beautiful ceramic plant pot set perfect for creating your indoor garden oasis.

Set Includes:
• 3 ceramic pots in graduated sizes (4", 6", 8")
• Drainage holes with matching saucers
• Modern minimalist design
• Neutral colors complement any decor
• Food-safe ceramic glaze
• Suitable for various plant types
• Easy to clean and maintain
• Gift-ready packaging

Transform your living space with these elegant planters that combine functionality with style.''',
                'image_url': 'https://images.unsplash.com/photo-1485955900006-10f4d324d411?w=400&h=300&fit=crop'
            },
            {
                'name': 'LED Desk Lamp',
                'description': '''Modern LED desk lamp with advanced features for optimal lighting and productivity.

Features:
• 24W LED with 2000 lumens brightness
• 3 color temperatures (3000K-6500K)
• 10 brightness levels for perfect ambiance
• USB charging port for devices
• Touch controls with memory function
• Adjustable arm and head (360° rotation)
• Eye-care technology reduces strain
• Energy efficient - 80% less power consumption

Perfect for office work, studying, reading, or any task requiring quality lighting.''',
                'image_url': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&h=300&fit=crop'
            },
            {
                'name': 'Yoga Mat',
                'description': '''Premium yoga mat designed for comfort, stability, and durability during your practice.

Features:
• 6mm thick high-density foam cushioning
• Non-slip texture on both sides
• 72" length x 24" width - extra room
• Eco-friendly TPE material
• Lightweight yet durable construction
• Easy to clean with soap and water
• Comes with carrying strap
• Odor-resistant and latex-free

Ideal for yoga, pilates, stretching, and floor exercises. Suitable for all skill levels.''',
                'image_url': 'https://images.unsplash.com/photo-1571019613540-996a378ba1f1?w=400&h=300&fit=crop'
            },
            {
                'name': 'Water Bottle',
                'description': '''Premium stainless steel water bottle with advanced insulation technology.

Features:
• Double-wall vacuum insulation
• Keeps drinks cold for 24 hours, hot for 12 hours
• 24oz capacity with wide mouth opening
• Leak-proof cap with convenient carry loop
• BPA-free and food-grade materials
• Sweat-proof exterior finish
• Compatible with most cup holders
• Easy to clean and dishwasher safe

Perfect for sports, travel, office, or daily hydration needs. Environmentally friendly alternative to plastic bottles.''',
                'image_url': 'https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=400&h=300&fit=crop'
            },
        ]

        for product_data in products_data:
            try:
                product = Product.objects.get(name=product_data['name'])
                product.description = product_data['description']
                # Note: In a real application, you would download and save the image
                # For now, we'll update the description and leave a note about the image
                product.save()
                self.stdout.write(f'Updated product: {product.name}')
            except Product.DoesNotExist:
                self.stdout.write(f'Product not found: {product_data["name"]}')

        self.stdout.write(
            self.style.SUCCESS('Successfully updated products with detailed descriptions!')
        )
        self.stdout.write(
            self.style.WARNING('Note: Image URLs provided in the data. In production, you would download and save these images.')
        )
