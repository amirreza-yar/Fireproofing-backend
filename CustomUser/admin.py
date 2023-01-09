from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import UserProfile
# from .forms import CustomUserCreationForm, CustomUserChangeForm

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = UserProfile
#     list_display = ['email',]

admin.site.register(UserProfile)

# from django.contrib import admin
# from .models import UserProfile

# admin.site.register(UserProfile)