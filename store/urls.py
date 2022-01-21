from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePageView, name='home'),
    path('shop/', views.shopPageView, name='shop'),
    path('cart/', views.cartPageView, name='cart'),
    path('checkout/', views.checkoutPageView, name='checkout'),

    path('update_item/', views.updateItem, name='update_item'),
    path('submit_checkout/', views.submitCheckout, name='submit_checkout')
]