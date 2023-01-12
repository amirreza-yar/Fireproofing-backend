from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.http.response import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages

import json

from Product.models import CartItem

from .models import Product as ProductModel
from .models import ProductComment
from .models import Cart as CartModel
from .models import CartItem as CartItemModel
from .models import Order as OrderModel
from .forms import MakeComment as MakeCommentForm
from .forms import AddToCart as AddToCartForm
from .forms import GetDestinationDetails as GetDestinationDetailsForm


def products(request):
    
    products = ProductModel.objects.all()

    context = {
        "title": "محصولات",
        "is_index_page": False,
        "products": products,
    }

    for product in products:
        print(product.name, sep="\n\n")
    return render(request, "products.html", context=context)

def productDetail(request, pk):

    product = get_object_or_404(ProductModel, pk=pk)
    product_comments = ProductComment.objects.all().filter(product=product)
    # product2 = ProductModel.objects.get(pk=pk).comments
    # print(product.comments.all())
    # print(product2)
    # print(comments)
    # product.comments.create(
    #     user=request.user,
    #     product=product,
    #     user_rate=4,
    #     commenter_name='امیررضا',
    #     commenter_email='example@example.com',
    #     comment='خیلی خوبه!',
    # )
    # product_comments = product.comments.all()
    # product = ProductModel.objects.get_o(pk=pk)
    # print(product.comments)
    # comment = ProductComment.objects.all()[0]
    # print(comment.product)
    # print(product_comments)

    try:
        product_cart_item = CartItem.objects.get(product=product)
        product_quantity = product_cart_item.quantity
    except:
        product_quantity = 1


    context = {
        "title": "محصولات",
        "is_index_page": False,
        "product": product,
        "product_comments": product_comments,
        "add_to_cart_form": AddToCartForm(None),
        "product_quantity": product_quantity,
    }
    return render(request, "productDetail.html", context=context)

@require_POST
def makeComment(request, pk):
    # print("I'm running!")
    # print(request.POST)
    comment_form = MakeCommentForm(request.POST)
    # print(comment_form)
    if comment_form.is_valid():
        # print(comment_form['comment'].value())
        ProductComment.objects.create(
            user=request.user,
            product=ProductModel.objects.get(pk=pk),
            commenter_name=comment_form['commenter_name'].value(),
            commenter_email=comment_form['commenter_email'].value(),
            comment=comment_form['comment'].value(),
        )

    # return HttpResponse('')
    return redirect('product', pk=pk)

def cart(request):
    
    # try:
    #     # print("I'm running!")
    #     cart = request.user.cart
    #     cart_items = cart.items.all()
    #     cart_finished_price = cart.finished_price
    #     print(cart_finished_price)
    # except:
    #     cart_items = None
    #     cart_finished_price = None

    # for item in cart_items:
    #     print(item.product.name)
    # data = serializers.serialize('json', cart_items)
    # print(data)

    # print(cart.items.all())
    context = {
        "title": "سبد خرید",
        "is_index_page": False,
        # "cart_items": cart_items,
        # "cart_finished_price": cart_finished_price,
    }
    return render(request, "cart.html", context=context)

@require_POST
def addToCart(request, pk):

    cart_item_form = AddToCartForm(request.POST or None)
    if cart_item_form.is_valid():
        print("its valid!")
        item_quantity = int(cart_item_form['quantity'].value())

        cart, created = CartModel.objects.get_or_create(customer=request.user)
        product = get_object_or_404(ProductModel, pk=pk)
        cart_item, created = CartItemModel.objects.get_or_create(product=product, cart=cart)
        if cart.items.filter(pk=cart_item.pk).exists():
            cart_item.quantity += item_quantity
            cart_item.save()
        else:
            cart.items.add(cart_item)
    # cart_item = CartItemModel.objects.create(product=product, cart=cart)

    return redirect("product", pk=pk)

@login_required(login_url='login')
@require_POST
def makeOrder(request):

    cart = CartModel.objects.get(customer=request.user)
    user = request.user
    # print(request.cart)
    destination_details_form = GetDestinationDetailsForm(request.POST)
    if destination_details_form.is_valid():
        
        postal_code = destination_details_form['postal_code'].value()
        address = destination_details_form['address'].value()
        print(postal_code, address)
        cart_items = cart.items.all()
        unseri_item = []

        # Jesonify the items, to store in user invoice
        for item in cart_items:
            unseri_item.append({
                "name": item.product.name,
                "pk": item.product.pk,
                "price": item.product.price,
                "quantity": item.quantity,
                "total_price": item.total_price,
            })

            item.product.add_to_quantity_purchased(item.quantity)

        json_items = json.dumps(unseri_item)

        OrderModel.objects.create(
            customer=user,
            address=address,
            items=json_items,
            postal_code=postal_code,
            shipping_price=cart.shipping_price,
            items_price=cart.items_price,
            finished_price=cart.finished_price,
            phone_number=user.phone_number
            # status=
            # discount_amount=0,
        )

    else:
        # send some error messages
        messages.error(request, "Wrong input!")
    
    # print(json.loads(json_items))
    # print(request.user.name)

    # print(request.postal_code)


    return HttpResponse(status=200)