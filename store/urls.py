from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePageView, name='home'),
    path('shop/', views.shopPageView, name='shop'),
    path('cart/', views.cartPageView, name='cart'),
    path('checkout/', views.checkoutPageView, name='checkout')
]