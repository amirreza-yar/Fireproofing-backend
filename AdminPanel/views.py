import json
from django.shortcuts import render
from django.views.generic import CreateView,UpdateView
from django.core.paginator import Paginator
from django.db.models import Count
from django.urls import reverse,reverse_lazy
from Blog.models import Blog
from CustomUser.models import UserProfile
from Product.models import Category, Order, Product
from .forms import BlogForm, CategoryForm, PersonelForm, ProductForm
def dashboard(request):
    context = {}
    sell_report = {
        'daily' : Order.objects.all().extra({'ordered_date':"date(ordered_date)"}).values('ordered_date').annotate(ordered_date_count=Count('id')),
        # 'monthly' : 
    }
    order_report = {
        'canceled' : Order.objects.filter(status='CD').count,
        'completed' : Order.objects.filter(status='RC').count
    }
    context['sell_report'] = sell_report
    context['order_report'] = order_report
    context['last_order'] = Order.objects.all()[:4]
    return render(request, 'admin/index.html', context)

#* PERSONEL BLOCK
def personel_list(request):
    context = {
        'personels' : UserProfile.objects.filter(is_active=True,is_staff=True).order_by('date_joined'),
    }
    return render(request, 'admin/listkarmand.html', context)
class personel_add(CreateView):
    model = UserProfile
    template_name = 'admin/addkarmand.html'
    form_class = PersonelForm
    success_url = reverse_lazy('adminP:personel_list')
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
    return render(request,'admin/addkarmand.html',context,status=status)
def delete_personel(request, personel):
    personel_obj:UserProfile = UserProfile.objects.get(id=personel)
    personel_obj.delete()
    return reverse('adminP:personel_list')

#* USERMANAGEMENT BLOCK
def user_list(request):
    page=request.GET.get('page',1)
    per_page=request.GET.get('per_page',6)
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
    return render(request, 'admin/userlist.html', context)

#* CATEGORY BLOCK
class category(CreateView):
    model = Category
    template_name = 'admin/category.html'
    form_class = CategoryForm
    success_url = reverse_lazy('adminP:category')
    def get_context_data(self, **kwargs):
        data = kwargs
        data['listcat'] = Category.objects.all()
        print(data)
        return super().get_context_data(**data)
#* WEBLOG MANAGEMENT BLOCK
def weblog_list(request):
    #! NO PAGINATION, NO SEARECH, NO FILTERS??
    context = {
        'blogs' : Blog.objects.all().order_by('released_date')
    }
    return render(request, 'admin/bloglist.html', context)
class weblog_edit(UpdateView):
    template_name = 'admin/addblog.html'
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('adminP:weblog_list')
class weblog_add(CreateView):
    template_name = 'admin/addblog.html'
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('adminP:weblog_list')
def weblog_delete(request,pk):
    try:
        blog = Blog.objects.get(id=pk)
        blog.delete()
        return reverse('adminP:weblog_list')
    except Blog.DoesNotExist:
        return reverse('404')

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
    return render(request, 'admin/productlist.html', context)

class product_add(CreateView):
    template_name = 'admin/addproduct.html'
    model = Product
    success_url = reverse_lazy('adminP:product_list')
    form_class = ProductForm

class product_edit(UpdateView):
    model = Product
    template_name = 'admin/addproduct.html'
    success_url = reverse_lazy('adminP:product_list')
    form_class = ProductForm
#* ORDER BLOCK
def order_list(request):
    orders = Order.objects.all()
    context = {
        'orders' : orders,
    }
    return render(request,'admin/orderlist.html',context)
def order_detail(request, pk):
    order = Order.objects.get(id=pk)
    context = {'order': order, 'items': order.loaded_json_items()}
    return render(request,'admin/orderdetail.html',context)
def order_cancel(request, pk):
    order = Order.objects.get(id=pk)
    order.status = 'CD'
    order.save()
    orders = Order.objects.all()
    context = {
        'orders' : orders,
    }
    return render(request,'admin/orderlist.html',context)
#* AGENTS BLOCK
#! CAN'T FIND MODEL !! :|
