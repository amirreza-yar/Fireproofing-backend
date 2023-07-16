from django.shortcuts import render, redirect
from CustomUser.models import UserProfile as userProfileModel
from Product.models import Product,Category

def contactUs(request):
    return render(request, "contact-us.html", {"title": "ارتباط با ما", "is_index_page": False})

def aboutUs(request):
    return render(request, "about-us.html", {"title": "درباره ما", "is_index_page": False})

def faq(request):
    return render(request, "faq.html", {"title": "سوالات متداول", "is_index_page": False})

def hamkari(request):
    return render(request, "hamkari.html", {"title": "همکاری", "is_index_page": False})

def namaiandegi(request):
    return render(request, "namaiandegi.html", {"title": "نمایندگی ها", "is_index_page": False})

def rules(request):
    return render(request, "rules.html", {"title": "قوانین", "is_index_page": False})

def index(request):
    # print(request.user)
    # print(request.session['lang'])
    # print(request.session['lang'] == True)
    # print(request.user.id)
    context = {
        "title": "فروشگاه آتش‌نبرد",
        "is_index_page": True,
        "categories": Category.objects.filter(parent=None),
        "products": Product.objects.all(),
        }
    return render(request, "index.html",context=context )

def error404Handler(request, exception):
    # print("I'm running!")
    return render(request, "404error.html", {"title": "ارور ۴۰۴", "is_index_page": False})

def switchLang(request, pk):


    if pk == 0:
        request.session['lang'] = False
    elif pk == 1:
        request.session['lang'] = True

    print("lang is:", request.session['lang'] == True)

    return redirect('index')