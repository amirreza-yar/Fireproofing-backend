from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('userProfile', views.userProfile, name="userProfile"),
    path('editProfile', views.editProfile, name="editProfile"),
    path('userHistory', views.userHistory, name="userHistory"),
    path('logout', views.logout, name="logout"),
    path('userInvoice/<int:pk>', views.userInvoice, name="userInvoice"),
]