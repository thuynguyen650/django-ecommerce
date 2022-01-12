from django.shortcuts import render

# Create your views here.
def homePageView(request):
    return render(request, 'store/home.html')

def shopPageView(request):
    return render(request, 'store/shop.html')

def cartPageView(request):
    return render(request, 'store/cart.html')

def checkoutPageView(request):
    return render(request, 'store/checkout.html')