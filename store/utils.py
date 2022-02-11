#this file store some helper functions
import json
from .models import *

# handle guest cart 
def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart']) #get product id and product quantity from cart cookie
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
    
# handle cart data 
def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, completed=False)
        order_items = order.orderitem_set.all()
    else:
        cookieData = cookieCart(request)
        order = cookieData['order']
        order_items = cookieData['order_items']
    context = {
        'order_items': order_items,
        'order': order
    }
    return context

# guest checkout function
def guestOrder(request, data):
    # create customer
    customer, created = Customer.objects.get_or_create(email=data['customerInfo']['email'])
    customer.name = data['customerInfo']['name']
    customer.telephone = data['customerInfo']['phone']
    customer.save()

    #create order
    order = Order.objects.create(customer=customer, completed=False)

    #create order items
    order_items = cartData(request)['order_items']
    for order_item in order_items:
        product = Product.objects.get(id=order_item['product']['id'])
        print(product)
        OrderItem.objects.create(
            product=product,
            order=order,
            quantity=order_item['quantity']
        )
    return customer, order