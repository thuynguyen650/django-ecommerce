from django.shortcuts import render
from .models import (
    Product,
    OrderItem,
    Order
)
# Create your views here.
def homePageView(request):
    return render(request, 'store/home.html')

def shopPageView(request):
    products = Product.objects.all()
    return render(request, 'store/shop.html', {'products': products})

def cartPageView(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer)
        order_items = order.orderitem_set.all() #parent.child_set.all()
    else:
        order_items = []
        order = {'get_subtotal': 0}
    context = {
        'order_items': order_items,
        'order': order
    }
    return render(request, 'store/cart.html', context)

def checkoutPageView(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer)
        order_items = order.orderitem_set.all()
    else:
        order_items = []
        order = {'get_subtotal':0}
    context = {
        'order_items': order_items,
        'order': order
    }
    return render(request, 'store/checkout.html', context)