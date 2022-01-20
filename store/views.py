from itertools import product
from django.shortcuts import render
from .models import (
    Product,
    OrderItem,
    Order
)
from django.http import JsonResponse
import json

# Create your views here.
def homePageView(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer)
    else:
        order = {'get_total': (0,0)}
    return render(request, 'store/home.html', {'order': order})

def shopPageView(request):
    products = Product.objects.all()
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer)
    else:
        order = {'get_total': (0,0)}
    context = {
        'order': order,
        'products': products
    }
    return render(request, 'store/shop.html', context)

def cartPageView(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer)
        order_items = order.orderitem_set.all() #parent.child_set.all()
    else:
        order_items = []
        order = {'get_total': (0,0)}
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

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action  = data['action']
    product = Product.objects.get(id = productId)
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer = customer)
    order_item, created = OrderItem.objects.get_or_create(product = product, order = order)
    if action == 'add':
        order_item.quantity += 1
    elif action == 'remove':
        order_item.quantity -= 1
    order_item.save()
    if order_item.quantity == 0:
        order_item.delete()
    return JsonResponse({
        'subtotal': order.get_subtotal()
    })