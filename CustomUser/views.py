from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http.response import JsonResponse, HttpResponseForbidden
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from .forms import UserRegisterForm, UserUpdateForm
from .models import UserProfile as userProfileModel

from Product.models import Order as OrderModel

# TODO Edit profile page
# TODO Show error messages

def register(request):
    if request.user.is_authenticated:
        return redirect('index')

    registerForm = UserRegisterForm(request.POST or None)
    # print(registerForm)
    # print("Before validation...")
    if registerForm.is_valid ():
        # print("I't valid")
        # messages.success (request, "account created succesfully!")
        registerForm.save()
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(username=username, password=password)
        auth_login(request, user)
        # request.session['email'] = email
        # request.session['name'] = name
        # print(user)
        # messages.success (request, "Your account created successfuly, logging in to messenger ...")
        return redirect('userProfile')


    context = {
        "title": "ثبت نام",
        "is_index_page": False,
        "register_form": registerForm,
    }
    # print(request.session['email'])
    return render(request, 'register.html', context=context)

@login_required(login_url='login')
def logout(request):
    auth_logout(request)
    # request.session.flush()

    return redirect('index')


# TODO 
def login(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.POST:
        name = request.POST['name']
        password = request.POST['password1']
        user = authenticate(username=name, password=password)
        if user:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.error(request, "نام کاربری یا رمز اشتباه است!")
        # request.session['email'] = email
        # request.session['name'] = name
        

    return render(request, 'login.html', {"title": "ورود", "is_index_page": False})

@login_required(login_url='login')
def userProfile(request):

    context = {
        "title": "پروفایل",
        "is_index_page": False,
        # "userProfile": user,
    }

    return render(request, "userProfile.html", context=context)

@login_required(login_url='login')
def editProfile(request):

    updateForm = UserUpdateForm(request.POST, instance=request.user)
    if request.method == 'POST':
        # user_form = UpdateUserForm(request.POST, instance=request.user)
        # profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        print(updateForm.is_valid())
        # print(request.POST)
        for field in updateForm:
            print(field)
            print(field.errors)

        
        if updateForm.is_valid():
            print("I'ts valid!")
            print(updateForm)
            updateForm.save()
            messages.success(request, 'Your profile is updated successfully')
            # return None
            return redirect('userProfile')
        else:

            messages.error(request, "Wrong input data!")
            context = {
                "title": "ویرایش پروفایل",
                "is_index_page": False,
                "update_form": updateForm,
            }
            return render(request, "editProfile.html", context=context)


    context = {
            "title": "ویرایش پروفایل",
            "is_index_page": False,
    }


    return render(request, "editProfile.html", context=context)

    # updateForm = UserUpdateForm(instance=request.user)
        # profile_form = UpdateProfileForm(instance=request.user.profile)

    # return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required(login_url='login')
def userHistory(request):

    invoices = OrderModel.objects.all()
    # print(invoices[0].get_status_display())
    context = {
        "title": "تاریخچه کاربر",
        "is_index_page": False,
        "invoices": invoices,
    }

    return render(request, "userHistory.html", context=context)

def userInvoice(request, pk):
    invoice = OrderModel.objects.get(pk=pk)
    # print(request.user.postal_code)

    # items = invoice.loaded_json_items

    context = {
        "invoice": invoice,
        "title": f"فکتور شماره {invoice.pk}",
    }
    return render(request, "userInvoice.html", context=context)