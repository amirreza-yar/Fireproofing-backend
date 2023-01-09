from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http.response import JsonResponse, HttpResponseForbidden
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from .forms import UserRegisterForm
from .models import UserProfile as userProfileModel

def register(request):
    if request.user.is_authenticated:
        return redirect('index')

    registerForm = UserRegisterForm(request.POST or None)
    # print(registerForm)
    # print("Before validation...")
    if registerForm.is_valid ():
        # print("I't valid")
        # messages.success (request, "account created succesfully!")
        registerForm.save ()
        email = request.POST['email']
        password = request.POST['password1']
        user = authenticate(username=email, password=password)
        auth_login(request, user)
        # request.session['email'] = email
        # print(user)
        # messages.success (request, "Your account created successfuly, logging in to messenger ...")
        return redirect('index')


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
    request.session.flush()

    return redirect('index')


def login(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.POST:
        email = request.POST['email']
        password = request.POST['password1']
        user = authenticate(username=email, password=password)
        auth_login(request, user)
        request.session['email'] = email
        
        return redirect('index')

    return render(request, 'login.html', {"title": "ورود", "is_index_page": False})

@login_required(login_url='login')
def userProfile(request):
    # print(request.session['email'])
    user = userProfileModel.objects.get(email__exact=request.session['email'])
    print(user.email)
    context = {
        "title": "پروفایل",
        "is_index_page": False,
        "userProfile": user,
    }
    # print(request.GET['username'])
    # print(userProfileModel.address)
    return render(request, "userProfile.html", context=context)

def editProfile(request):

    return render(request, "editProfile.html", {"title": "ویرایش پروفایل", "is_index_page": False})

def userHistory(request):

    return render(request, "userHistory.html", {"title": "تاریخچه کاربر", "is_index_page": False})