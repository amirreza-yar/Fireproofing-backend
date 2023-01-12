from django.urls import path

from . import views

urlpatterns = [
    path('products', views.products, name='products'),
    path('product/<int:pk>', views.productDetail, name='product'),
    path('addToCart/<int:pk>', views.addToCart, name='addToCart'),
    path('cart', views.cart, name='cart'),
    path('makeOrder', views.makeOrder, name='makeOrder'),
    path('makeComment/<int:pk>', views.makeComment, name='makeComment'),
]