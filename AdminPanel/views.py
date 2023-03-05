from django.shortcuts import render,get_object_or_404, redirect
from django.core.paginator import Paginator
from Blog.models import Blog
from CustomUser.models import UserProfile
from Product.models import Category, Order
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
    #! NEED TO ADD `is_deleted` FIELD IN MODEL
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
    # ! DATABASE AND FRONTEND ARE NOT SYNC
    # create category with select choices or with desceiption
    # desceiption is recommende
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
        blog = Blog.objects.get(id=pk)
        #! DB NOT SYNC WITH FRONTEND
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
        blog = Blog(**request.POST) #! DB NOT SYNC WITH FRONTEND
        blog.save()
        return redirect('blogList')
    else:
        status = 200
    return render(request, 'editblog.html', context, status=status)
def weblog_delete(request,pk):
    try:
        blog = Blog.objects.get(id=pk)
        blog.delete()
        return redirect('blogList')
    except Blog.DoesNotExist:
        return redirect('404')

#* PRODUCT BLOCK
#! DATABASE NOT SYNC WITH ANYTHING :(
# any product needs one image or more?

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
    pass #! DB NOT SYNC :(

#* AGENTS BLOCK
#! CAN'T FIND MODEL !! :|
