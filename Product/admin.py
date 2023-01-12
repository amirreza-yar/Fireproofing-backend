from django.contrib import admin

from .models import Product, Cart, CartItem, Order, ProductComment

admin.site.register(Product)
admin.site.register(ProductComment)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)