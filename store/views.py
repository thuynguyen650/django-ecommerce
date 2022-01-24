from itertools import product
from django.shortcuts import render
from .models import (
    Product,
    OrderItem,
    Order,
    ShippingAddress
)
from django.http import JsonResponse
import json
import datetime
from .utils import cookieCart

# Create your views here.
def homePageView(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, completed=False)
    else:
        cookieData = cookieCart(request)
        order = cookieData['order']
    return render(request, 'store/home.html', {'order': order})

def shopPageView(request):
    products = Product.objects.all()
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, completed=False)
    else:
        cookieData = cookieCart(request)
        order = cookieData['order']
    context = {
        'order': order,
        'products': products
    }
    return render(request, 'store/shop.html', context)

def cartPageView(request):
    print(cookieCart(request))
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, completed=False)
        order_items = order.orderitem_set.all() #parent.child_set.all()
    else:
        cookieData = cookieCart(request)
        order = cookieData['order']
        order_items = cookieData['order_items']
    context = {
        'order_items': order_items,
        'order': order
    }
    return render(request, 'store/cart.html', context)

def checkoutPageView(request):
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
    return render(request, 'store/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action  = data['action']
    product = Product.objects.get(id = productId)
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer = customer, completed=False)
    order_item, created = OrderItem.objects.get_or_create(product = product, order = order)
    if action == 'add':
        order_item.quantity += 1
    elif action == 'remove':
        order_item.quantity -= 1
    order_item.save()
    if action == 'delete' or order_item.quantity == 0:
        order_item.delete()
    return JsonResponse({
        'subtotal': order.get_subtotal()
    })

def submitCheckout(request):
    data = json.loads(request.body)
    if request.user.is_authenticated:
        transaction_id = datetime.datetime.now()
        customer = request.user.customer
        order = Order.objects.get(customer=customer, completed=False)
        order.transaction_id = transaction_id
        if float(data['formInfo']['total']) == order.get_subtotal():
            order.completed = True
        order.save()
        ShippingAddress.objects.create(
            order = order,
            customer = customer,
            address = data['formInfo']['address'],
            province = data['formInfo']['province'],
            district = data['formInfo']['district'],
            commune = data['formInfo']['commune']
        )

    else:
        print('User is not log in')
    return JsonResponse(data['formInfo'], safe=False)