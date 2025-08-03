# E-Commerce Store

A fully functional e-commerce web application built with Django (Python) for the backend and Bootstrap for the frontend.

## Features

### 🛍️ Core E-commerce Features
- **Product Catalog**: Browse products by categories with pagination
- **Product Details**: Detailed product pages with descriptions, pricing, and stock information
- **Shopping Cart**: Add/remove items, update quantities, persistent cart across sessions
- **Order Processing**: Complete checkout process with billing information
- **User Authentication**: Registration, login, logout functionality
- **User Profiles**: Manage personal information and view order history

### 📱 User Interface
- **Responsive Design**: Mobile-friendly interface using Bootstrap 5
- **Modern UI**: Clean and intuitive design with Font Awesome icons
- **Product Search**: Easy navigation through categories
- **Shopping Cart Badge**: Real-time cart item counter in navigation

### 🔧 Admin Features
- **Django Admin**: Full admin interface for managing products, categories, orders, and users
- **Product Management**: Add/edit products with images, categories, and inventory
- **Order Management**: View and update order statuses
- **User Management**: Manage user accounts and profiles

## Technology Stack

### Backend
- **Django 5.2.4**: Python web framework
- **SQLite**: Database (can be easily switched to PostgreSQL/MySQL)
- **Pillow**: Image handling for product photos

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Custom styling with Bootstrap framework
- **JavaScript**: Interactive functionality
- **Bootstrap 5**: Responsive CSS framework
- **Font Awesome**: Icon library

## Project Structure

```
ecommerce_store/
├── ecommerce_store/          # Main project settings
├── products/                 # Product catalog app
├── cart/                     # Shopping cart functionality
├── orders/                   # Order processing
├── accounts/                 # User authentication and profiles
├── templates/                # HTML templates
├── static/                   # CSS, JavaScript, images
├── media/                    # User uploaded files
└── manage.py                 # Django management script
```

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Steps

1. **Clone or download the project**
   ```bash
   cd Task-1
   ```

2. **Install required packages**
   ```bash
   pip install django pillow
   ```

3. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create a superuser (admin account)**
   ```bash
   python manage.py createsuperuser
   ```

5. **Populate database with sample data**
   ```bash
   python manage.py populate_db
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Usage Guide

### For Customers

1. **Browse Products**
   - Visit the homepage to see all products
   - Use category sidebar to filter products
   - Click on products to view detailed information

2. **Shopping Cart**
   - Add products to cart from product listing or detail pages
   - View cart by clicking the cart icon in navigation
   - Update quantities or remove items as needed

3. **User Account**
   - Register for a new account or login
   - View and edit profile information
   - Check order history

4. **Place Orders**
   - Add items to cart and proceed to checkout
   - Fill in billing information
   - Complete the order

### For Administrators

1. **Access Admin Panel**
   - Login at `/admin/` with superuser credentials

2. **Manage Products**
   - Add new products with images and descriptions
   - Create and manage product categories
   - Update stock levels and pricing

3. **Process Orders**
   - View incoming orders
   - Update order statuses (pending → processing → shipped → delivered)
   - Manage customer information

## Database Models

### Products App
- **Category**: Product categories with name, slug, and description
- **Product**: Main product model with pricing, stock, and category relationship
- **ProductReview**: Customer reviews and ratings

### Cart App
- **Cart**: Shopping cart for users and anonymous sessions
- **CartItem**: Individual items in the cart with quantities

### Orders App
- **Order**: Customer orders with billing information and status
- **OrderItem**: Individual products within an order

### Accounts App
- **UserProfile**: Extended user information (address, phone, etc.)

## Customization

### Adding New Features
- The modular Django app structure makes it easy to add new functionality
- Each app (products, cart, orders, accounts) is self-contained
- Templates use Bootstrap classes for easy styling modifications

### Configuration
- Update `settings.py` for database, email, or media file configurations
- Modify `static/css/style.css` for custom styling
- Update `static/js/main.js` for additional JavaScript functionality

## Security Features

- CSRF protection on all forms
- User authentication for sensitive operations
- Secure password handling with Django's built-in authentication
- Session management for shopping carts

## Future Enhancements

Potential improvements for the application:
- Payment gateway integration (Stripe, PayPal)
- Email notifications for orders
- Product search functionality
- Wishlist feature
- Product reviews and ratings system
- Inventory management alerts
- Multi-vendor support
- API endpoints for mobile app integration

## Support

For questions or issues:
1. Check the Django documentation: https://docs.djangoproject.com/
2. Review the code comments for implementation details
3. Test with the sample data provided

## License

This project is created for educational purposes as part of a coding assignment.
