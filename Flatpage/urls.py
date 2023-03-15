from django.urls import path
from . import views

urlpatterns = [
    path('contact-us', views.contactUs, name="contact-us"),
    path('about-us', views.aboutUs, name="about-us"),
    path('faq', views.faq, name="faq"),
    path('hamkari', views.hamkari, name="hamkari"),
    path('namaiandegi', views.namaiandegi, name="namaiandegi"),
    path('rules', views.rules, name="faq"),
    # path('', views.index, name='index'),

    ## Temporary urls, will moved to their app next...
    path('', views.index, name="index"),
    path('switch-lang/<int:pk>', views.switchLang, name="switch-lang")
]

