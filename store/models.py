from contextlib import nullcontext
from re import sub
from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.ImageField(upload_to = 'product_img/',null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def imageURL(self):
        if self.image:
            return self.image.url
        return ''

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    transaction_id = models.IntegerField()

    def __str__(self):
        return str(self.transaction_id)

    def get_subtotal(self):
        order_items = self.orderitem_set.all()
        order_items_total = [order_item.get_total() for order_item in order_items]
        subtotal = sum(order_items_total)
        return subtotal

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    def get_total(self):
        return self.quantity * self.product.price


class ShippingAddress(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
    

