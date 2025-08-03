from .models import Cart


def cart(request):
    """
    Context processor to make cart available in all templates
    """
    cart_obj = None
    
    if request.user.is_authenticated:
        cart_obj, created = Cart.objects.get_or_create(user=request.user)
    elif request.session.session_key:
        cart_obj, created = Cart.objects.get_or_create(
            session_key=request.session.session_key
        )
    
    cart_items_count = 0
    cart_total = 0
    
    if cart_obj:
        cart_items_count = cart_obj.get_total_items()
        cart_total = cart_obj.get_total_price()
    
    return {
        'cart': cart_obj,
        'cart_items_count': cart_items_count,
        'cart_total': cart_total,
    }
