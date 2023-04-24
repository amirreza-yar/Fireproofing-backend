from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView,UpdateView
from django.core.paginator import Paginator
from django.db.models import Count
from django.urls import reverse,reverse_lazy
from django.contrib.auth import login, authenticate
from Blog.models import Blog
from CustomUser.models import UserProfile
from Product.models import Category, Order, Product
from .forms import BlogForm, CategoryForm, PersonelForm, ProductForm, LoginForm
def login_admin(request):
    form = LoginForm()
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('adminP:dashboard'))
            else:
                message = 'رمز عبود یا نام کاربری اشتباه است!'
    return render(
        request, 'admin/signin.html', context={'form': form, 'message': message})
def dashboard(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('adminP:login'))
    if not request.user.is_staff:
        return HttpResponseForbidden()
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

class Personel_Update(UpdateView):
    model = UserProfile
    template_name = 'admin/addkarmand.html'
    form_class = PersonelForm
    success_url = reverse_lazy('adminP:personel_list')
def delete_personel(request, personel):
    personel_obj:UserProfile = UserProfile.objects.get(id=personel)
    personel_obj.delete()
    return HttpResponseRedirect(reverse('adminP:personel_list'))

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
class Category_view(CreateView):
    model = Category
    template_name = 'admin/category.html'
    form_class = CategoryForm
    success_url = reverse_lazy('adminP:category')
    def get_context_data(self, **kwargs):
        data = kwargs
        data['listcat'] = Category.objects.all()
        print(data)
        return super().get_context_data(**data)

class CategoryEdit(UpdateView):
    model = Category
    template_name = 'admin/category.html'
    form_class = CategoryForm
    success_url = reverse_lazy('adminP:category')
    def get_context_data(self, **kwargs):
        data = kwargs
        data['listcat'] = Category.objects.all()
        print(data)
        return super().get_context_data(**data)

def category_delete(self, pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    return HttpResponseRedirect(reverse('adminP:category'))
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
