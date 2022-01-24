#this file store some helper functions
import json
from .models import *

def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
    order_items = []
    order = {
        'get_subtotal': 0,
        'get_items_total': 0
    }
    for item in cart:
        try:
            product = Product.objects.get(id=item)
            order_item = {
                'product': {
                    'name': product.name,
                    'price': product.price,
                    'id': product.id,
                    'image': {'url': product.image.url}
                },
                'quantity': cart[item]['quantity'],
                'get_total': product.price * cart[item]['quantity']
            }
            order['get_items_total'] += 1
            order['get_subtotal'] += order_item['get_total']
            order_items.append(order_item)
        except:
            #if product removed from database
            pass
    return {'order': order, 'order_items': order_items}
    