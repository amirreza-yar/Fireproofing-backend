from django.urls import path

from . import views

urlpatterns = [
    path('products', views.products, name='products'),
    path('product/<int:pk>', views.productDetail, name='product'),
    path('cart', views.cart, name='cart'),
    path('addToCart/<int:pk>', views.addToCart, name='addToCart'),
    path('deleteFromCart/<int:pk>', views.deleteFromCart, name='deleteFromCart'),
    path('makeOrder', views.makeOrder, name='makeOrder'),
    path('makeComment/<int:pk>', views.makeComment, name='makeComment'),
    path('pardakhtMovafaq', views.pardakhtMovafaq, name='pardakhtMovafaq'),
    path('pardakhtNaMovafaq', views.pardakhtNaMovafaq, name='pardakhtNaMovafaq'),
    path('khadamat', views.khadamat, name='khadamat'),
    path('khedmatDetail/<int:pk>', views.khedmatDetail, name='khedmatDetail'),
    path('addServiceToCart/<int:pk>', views.addServiceToCart, name='addServiceToCart'),
    path('discountCode', views.discountCode, name='discountCode'),
]