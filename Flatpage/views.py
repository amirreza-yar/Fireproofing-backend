from django.shortcuts import render

def contactUs(request):
    return render(request, "contact-us.html", {"title": "ارتباط با ما"})

def aboutUs(request):
    return render(request, "about-us.html", {"title": "درباره ما"})

def faq(request):
    return render(request, "faq.html", {"title": "سوالات متداول"})

def hamkari(request):
    return render(request, "hamkari.html", {"title": "همکاری"})

def namaiandegi(request):
    return render(request, "namaiandegi.html", {"title": "نمایندگی ها"})

def rules(request):
    return render(request, "rules.html", {"title": "قوانین"})

def index(request):
    return render(request, "index.html", {"title": "فروشگاه قلان"})

def error404Handler(request, exception):
    # print("I'm running!")
    return render(request, "404error.html", {"title": "ارور ۴۰۴"})