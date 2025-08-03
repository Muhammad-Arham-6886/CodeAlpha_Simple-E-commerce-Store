from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Category, Product


def home(request):
    """Home page with featured products and categories"""
    featured_products = Product.objects.filter(available=True)[:8]  # Latest 8 products
    categories = Category.objects.all()[:6]  # First 6 categories
    
    # Get some statistics
    total_products = Product.objects.filter(available=True).count()
    total_categories = Category.objects.count()
    
    return render(request, 'products/home.html', {
        'featured_products': featured_products,
        'categories': categories,
        'total_products': total_products,
        'total_categories': total_categories,
    })


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    # Pagination
    paginator = Paginator(products, 12)  # Show 12 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'products/list.html', {
        'category': category,
        'categories': categories,
        'products': page_obj,
    })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    reviews = product.reviews.all().order_by('-created_at')
    
    return render(request, 'products/detail.html', {
        'product': product,
        'reviews': reviews,
    })
