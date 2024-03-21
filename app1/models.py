from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import *
# Create your models here.
class CustomUser(AbstractUser):
    id = models.IntegerField(primary_key=True)

    username = None
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.IntegerField(blank=True,null=True)
    address = models.CharField(max_length=100)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name
class Category(models.Model):
    id = models.IntegerField(primary_key=True)

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Brand(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.IntegerField(primary_key=True)

    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10 ,decimal_places=2)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=100)
    size = models.ForeignKey(Size,on_delete=models.CASCADE)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE)
    def __str__(self):
        return self.name

    






class Order(models.Model):
    order_no = models.CharField(max_length=10)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    total_price = models.DecimalField(max_digits=10 ,decimal_places=2,null=True)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    country = models.CharField(max_length=10)
    state = models.CharField(max_length=10)
    zipcode = models.IntegerField()


    
    def __str__(self):
        return self.product.name

class OrderItem(models.Model): 
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10 ,decimal_places=2)
    total = models.DecimalField(max_digits=10 ,decimal_places=2)

    def __str__(self):
        return self.order.user.username

class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10 ,decimal_places=2 ,null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.name

class Wishlist(models.Model):
        user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
        quantity = models.PositiveIntegerField(default=1)

        product = models.ForeignKey(Product, on_delete=models.CASCADE) 

        def __str__(self):
            return self.product.name