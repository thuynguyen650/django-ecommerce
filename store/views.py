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
        order_items = order.orderitem_set.all()
    else:
        order_items = ''
    return render(request, 'store/cart.html', {'order_items': order_items})

def checkoutPageView(request):
    return render(request, 'store/checkout.html')