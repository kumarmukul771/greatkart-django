from .models import Cart2, CartItem2
from .views import _cart_id


def counter(request):
    cart_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart2.objects.filter(cart_id=_cart_id(request))
            if request.user.is_authenticated:
                cart_items = CartItem2.objects.all().filter(user=request.user)
            else:
                cart_items = CartItem2.objects.all().filter(cart=cart[:1])
            # for cart_item in cart_items:
            #     cart_count += cart_item.quantity
        except Cart2.DoesNotExist:
            cart_count = 0
    return dict(cart_count=cart_count)
