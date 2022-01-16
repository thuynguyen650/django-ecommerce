from django.shortcuts import render
from .models import (
    Product,
)
# Create your views here.
def homePageView(request):
    return render(request, 'store/home.html')

def shopPageView(request):
    products = Product.objects.all()
    return render(request, 'store/shop.html', {'products': products})

def cartPageView(request):
    return render(request, 'store/cart.html')

def checkoutPageView(request):
    return render(request, 'store/checkout.html')