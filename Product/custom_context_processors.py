# Context processor, to use cart model universally in all templates

from .models import Cart as CartModel

def cart_context(request):
    try:
        cart = CartModel.objects.get(customer=request.user)
        cart_items = cart.items.all()
    except:
        cart = None
        cart_items = None
    return {
        'cart': cart,
        'cart_items': cart_items,
    }