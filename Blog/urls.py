from django.urls import path

from . import views

urlpatterns = [
    path('blogs', views.blogs, name='blogs'),
    path('blog/<int:pk>', views.blogDetail, name='blog'),
    path('makeBlogComment/<int:pk>', views.makeBlogComment, name='makeBlogComment'),
]