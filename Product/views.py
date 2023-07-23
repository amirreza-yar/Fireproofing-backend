from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.http.response import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.db.models import Q

import json

from Product.models import CartItem
from .payment import ZarinRest
from .models import Product as ProductModel
from .models import ProductComment
from .models import Cart as CartModel
from .models import CartItem as CartItemModel
from .models import Order as OrderModel
from .models import Category as CategoryModel
from .forms import MakeComment as MakeCommentForm
from .forms import AddToCart as AddToCartForm
from .forms import GetDestinationDetails as GetDestinationDetailsForm
from .forms import DiscountCodeForm
from .models import DiscountCode as DiscountCodeModel

def products(request):

    try:
        request.session['lang']
    except:
        request.session["lang"] = 0

    # Filter the DB objects with given category or searhced text
    all_products = ProductModel.objects.all().filter(is_service=False)
    categories = CategoryModel.objects.all()
    products = int()
    categories_selected = list()

    try:
        searched_text = request.GET['search-text']
        if request.session["lang"]:
            searched_products = ProductModel.objects.filter(
                Q(en_name__icontains=searched_text) | Q(en_full_description__icontains=searched_text) | Q(en_meta_description__icontains=searched_text)
            )
        else:
            searched_products = ProductModel.objects.filter(
                Q(name__icontains=searched_text) | Q(full_description__icontains=searched_text) | Q(meta_description__icontains=searched_text)
            )
    except:
        searched_text = None
        products = None


    if request.session["lang"]:
        for category_name in list(request.GET):
            if categories.filter(en_name=category_name).exists():
                categories_selected.append(category_name)

        if len(categories_selected) >= 1:
            filters = Q(categories__en_name=categories_selected[0])

            for category_pk in range(1, len(categories_selected)):
                filters |= Q(categories__en_name=categories_selected[category_pk])

            products = all_products.filter(filters)
        else:
            products = all_products

    else:
        for category_name in list(request.GET):
            if categories.filter(name=category_name).exists():
                categories_selected.append(category_name)

        if len(categories_selected) >= 1:
            filters = Q(categories__name=categories_selected[0])
    
            for category_pk in range(1, len(categories_selected)):
                filters |= Q(categories__name=categories_selected[category_pk])

            products = all_products.filter(filters)
        else:
            products = all_products

    if searched_text:
        products = searched_products

    context = {
        "title": "محصولات",
        "is_index_page": False,
        "searched_text": searched_text,
        # "searched_products": searched_products,
        "products": products,
        "categories": categories,
        "categories_selected": categories_selected,
    }

    return render(request, "products.html", context=context)

def productDetail(request, pk):

    product = get_object_or_404(ProductModel, pk=pk, is_service=False)
    product_comments = ProductComment.objects.all().filter(product=product)

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

@login_required(login_url='login')
@require_POST
def makeComment(request, pk):
    comment_form = MakeCommentForm(request.POST)
    if comment_form.is_valid():
        ProductComment.objects.create(
            user=request.user,
            product=ProductModel.objects.get(pk=pk),
            commenter_name=comment_form['commenter_name'].value(),
            commenter_email=comment_form['commenter_email'].value(),
            comment=comment_form['comment'].value(),
        )


    # return HttpResponse('')
    return redirect('product', pk=pk)

@login_required(login_url='login')
def cart(request):
    
    cart = CartModel.objects.get_or_create(customer=request.user)
    context = {
        "title": "سبد خرید",
        "is_index_page": False,
    }
    return render(request, "cart.html", context=context)

@login_required(login_url='login')
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
def deleteFromCart(request, pk):

    try:
        item_to_delete = CartItemModel.objects.filter(pk=pk).delete()
        print(item_to_delete)
        messages.success(request, "Item have been deleted!")
    except:
        messages.success(request, "Item haven't been deleted!")

    return redirect("cart")


@login_required(login_url='login')
@require_POST
def makeOrder(request):

    user = request.user
    cart = CartModel.objects.get(customer=user)
    destination_details_form = GetDestinationDetailsForm(request.POST)
    if destination_details_form.is_valid():
        
        postal_code = destination_details_form['postal_code'].value()
        address = destination_details_form['address'].value().encode("UTF-8")
        cart_items = cart.items.all()
        unseri_item = []

        # Jesonify the items, to store in user invoice
        for item in cart_items:
            unseri_item.append({
                "name": item.product.name,
                "pk": item.product.pk,
                "price": item.product.get_price(),
                "quantity": item.quantity,
                "total_price": item.total_price,
            })

            item.product.add_to_quantity_purchased(value=item.quantity)

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

        zapi = ZarinRest("53946567-b7ac-47a9-8eec-adff5d3f2525",request.user.id)
        transaction = zapi.payment_request(int(str(cart.finished_price+"0")),"atashnabard payment process")
        
        cart.delete()
        return redirect(f"https://zarinpal.com/pg/StartPay/{transaction['data']['authority']}")
        
    else:
        # send some error messages
        messages.error(request, "Wrong input!")

        # Some paying backend
        return redirect("pardakhtNaMovafaq")
def verify_payment_proc(request,order_id):
    Status = request.GET.get('Status')
    Authority = request.GET.get('Authority')
    order = OrderModel.objects.get(id=order_id)
    amount = order.finished_price
    user = order.customer
    if Status == "OK":
        zapi = ZarinRest("53946567-b7ac-47a9-8eec-adff5d3f2525",order_id)
        transaction = zapi.verify_payment(amount,Authority)
        if transaction['data']['message'] == 'Paid':
            order.status = 'PN'
        elif transaction['data']['message'] == 'Verified':
            order.status = 'PN'
        else:
            order.status = 'UN'
            print(transaction['data'],f"==> {order_id}")
        order.save()
        return redirect('cart')

def pardakhtMovafaq(request):
    return render(request, "pardakhtmovafaq.html")

def pardakhtNaMovafaq(request):
    return render(request, "pardakhtnamovafaq.html")


def khadamat(request):
    services = ProductModel.objects.all().filter(is_service=True)

    context = {
    "title": "محصولات",
    "is_index_page": False,
    "services": services,
    }

    return render(request, "khadamat.html", context=context)

def khedmatDetail(request, pk):
    service = get_object_or_404(ProductModel, pk=pk, is_service=True)
    service_comments = ProductComment.objects.all().filter(product=service)

    context = {
        "title": "محصولات",
        "is_index_page": False,
        "service": service,
        "service_comments": service_comments,
        "add_to_cart_form": AddToCartForm(None),
        # "product_quantity": product_quantity,
    }
    return render(request, "khedmatDetail.html", context=context)

def addServiceToCart(request, pk):
    cart, created = CartModel.objects.get_or_create(customer=request.user)
    service = get_object_or_404(ProductModel, pk=pk, is_service=True)
    cart_item, created = CartItemModel.objects.get_or_create(product=service, cart=cart)

    if cart.items.filter(pk=cart_item.pk).exists():
        messages.error(request, "This item already exists!")
    else:
        cart.items.add(cart_item)
    
    return redirect("khedmatDetail", pk=pk)

@login_required(login_url="login")
@require_POST
def discountCode(request):
    # discount = DiscountCodeForm(request.POST or None)
    input_code = request.POST['code']
    
    discount_code = DiscountCodeModel.objects.filter(code=input_code)

    if discountCode.exists() and not discount_code.is_expired:

        messages.success(request, "Discount code is valid!")
        return redirect('cart')
    
    else:
        messages.error(request, "Discount code isn't valid!")
        return redirect('cart')