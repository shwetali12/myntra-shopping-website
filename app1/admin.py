from django.contrib import admin
from app1.models import CustomUser,Product,Cart,Category,Brand,Size,Color,Wishlist,Order,OrderItem
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Wishlist)
admin.site.register(Order)
admin.site.register(OrderItem)