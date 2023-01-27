from django.contrib import admin

from .models import Product, Cart, CartItem, Order, ProductComment, Category, DiscountCode

admin.site.register(Product)
admin.site.register(ProductComment)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(DiscountCode)