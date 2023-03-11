import json
from django.shortcuts import render,get_object_or_404, redirect
from django.core.paginator import Paginator
from Blog.models import Blog
from CustomUser.models import UserProfile
from Product.models import Category, Order, Product
from .forms import PersonelForm
def dashboard(request):
    context = {} #TODO: ask project manager for date needs to be use in panel
    return render(request, 'index.html', context)

#* PERSONEL BLOCK
def personel_list(request):
    context = {
        'personels' : UserProfile.objects.filter(is_active=True,is_staff=True).order_by('date_joined'),
    }
    return render(request, 'listkarmand.html', context)
def personel_add(request):
    personel_form = PersonelForm(request.POST or None)

    if personel_form.is_valid():
        personel_form.save()
        return redirect() #TODO: redirect to personal list
def update_info_personel(request, personel):
    updated_info = PersonelForm(request.POST, instance=UserProfile.objects.get(id=personel))
    context = {}
    status = 200
    if request.method == 'POST':
        if updated_info.is_valid():
            updated_info.save()
            context['status'] = 'ok'
            context['message'] = 'personel profile updated successfully'
            context['personel'] = updated_info
            status = 201
        else:
            context['status'] = 'error'
            context['message'] = 'wrong input data'
            context['personel'] = updated_info
            status = 418
    else:
        context['title'] = 'ویرایش پروفایل'
    return render(request,'addkarmand.html',context,status=status)
def delete_personel(request, personel):
    personel_obj:UserProfile = UserProfile.objects.get(id=personel)
    personel_obj.delete()

#* USERMANAGEMENT BLOCK
def user_list(request,page=None,per_page=6):
    all_users = UserProfile.objects.filter(is_staff=False).order_by('username')
    paginator = Paginator(all_users, per_page=per_page)
    users = paginator.get_page(page)
    context = {
        'users' : users, #TODO: processe in template tags
        'per_page' : per_page,
        'count_users' : paginator.count,
        'count_pages' : paginator.num_pages,
        'this_page' : page,
        'elided_pages' : paginator.get_elided_page_range(page,on_each_side=2)
    }
    return render(request, 'userlist.html', context)

#* CATEGORY BLOCK
def category_dashboard(request):
    context = {}
    categories = Category.objects.all()
    status = 0
    if request.method == 'GET':
        submit = request.GET.get('submit',None)
        if submit:
            text = request.GET.get('text',None)
            fulldescription = request.GET.get('fulldescription',None)
            if text and fulldescription:
                try:
                    cat = Category(text,fulldescription)
                    cat.save()
                    context = {
                        'step' : 'create-cat',
                        'msg' : 'success',
                        'list-cat' : categories,
                    }
                    status = 201
                except Exception as e:
                    context = {
                        'step' : 'create-cat',
                        'msg' : e,
                        'list-cat' : categories,
                    }
                    status = 500
            else:
                context = {
                            'step' : 'create-cat',
                            'msg' : 'error-all fields are required',
                            'list-cat' : categories,
                        }
                status = 400
    else:
        context = {
                    'step' : 'dashboard',
                    'list-cat' : categories,
                }
        status = 400
    return render(request, 'category.html', context, status)

#* WEBLOG MANAGEMENT BLOCK
def weblog_list(request):
    #! NO PAGINATION, NO SEARECH, NO FILTERS??
    context = {
        'blogs' : Blog.objects.all().order_by('released_date')
    }
    return render(request, 'bloglist.html', context, 200)
def weblog_edit(request,pk):
    context = {}
    status = 0
    if request.method == 'POST':
        data = json.loads(request.POST)
        blog = Blog.objects.get(id=pk)
        blog.cover = data['cover']
        blog.title = data['title']
        blog.en_title = data['en_title']
        blog.body = data['body']
        blog.en_body = data['en_body']
        blog.meta_description = data['meta_description']
        blog.en_meta_description = data['en_meta_description']
        blog.save()
        return redirect('blogList')
    else:
        context = {
            'blog': Blog.objects.get(id=pk),
        }
        status = 200
    return render(request, 'editblog.html', context, status=status)
def weblog_add(request,pk):
    context = {}
    status = 0
    if request.method == 'POST':
        data = json.loads(request.POST)
        del data['csrf_token']
        blog = Blog(**data)
        blog.save()
        return redirect('blogList')
    else:
        status = 200
    return render(request, 'addblog.html', context, status=status)
def weblog_delete(request,pk):
    try:
        blog = Blog.objects.get(id=pk)
        blog.delete()
        return redirect('blogList')
    except Blog.DoesNotExist:
        return redirect('404')

#* PRODUCT BLOCK
def product_list(request):
    per_page = request.GET.get('per_page',1)
    page = request.GET.get('page',1)
    products = Product.objects.all()
    paginator = Paginator(products, per_page=per_page)
    product_page = paginator.get_page(page)
    context = {
        'products' : product_page, #TODO: processe in template tags
        'per_page' : per_page,
        'count_obj' : paginator.count,
        'count_pages' : paginator.num_pages,
        'this_page' : page,
        'elided_pages' : paginator.get_elided_page_range(page,on_each_side=2)
    }
    return render(request, 'addproduct.html', context)

def product_add(request):
    context = {}
    status = 0
    if request.method == 'POST':
        data = json.loads(request.POST)
        del data['csrf_token']
        product = Product(**data)
        product.save()
        return redirect('blogList')
    else:
        status = 200
    return render(request, 'addproduct.html', context, status=status)

def product_edit(request, pk):
    if request.method == 'POST':
        data = json.loads(request.POST)
        product = Product.objects.get(id=pk)
        product.name = data['name']
        product.en_name = data['en_name']
        product.meta_description = data['meta_description']
        product.en_meta_description = data['en_meta_description']
        product.full_description = data['full_description']
        product.en_full_description = data['en_full_description']
        product.price = data['price']
        product.quantity_purchased = data['quantity_purchased']
        product.categories = data['categories']
        product.image0 = data['image0']
        product.image1 = data['image1']
        product.image2 = data['image2']
        product.image3 = data['image3']
        product.image4 = data['image4']
        product.image5 = data['image5']
        product.image6 = data['image6']
        product.save()
        return redirect('productList')
    else:
        context = {
            'product': Product.objects.get(id=pk),
        }
        status = 200
    return render(request, 'editproduct.html', context, status=status)
#* ORDER BLOCK
def order_list(request):
    orders = Order.objects.all()
    context = {
        'orders' : orders,
    }
    return render(request,'orderlist.html',context)
def order_detail(request, pk):
    order = Order.objects.get(id=pk)
    return render(request,'orderdetail.html',order)
def order_cancel(request, pk):
    order = Order.objects.get(id=pk)
    order.status = 'CD'

#* AGENTS BLOCK
#! CAN'T FIND MODEL !! :|
