from django.urls import path

from . import views

urlpatterns = [
    path('projects', views.projects, name='projects'),
    path('project/<int:pk>', views.projectDetail, name='project'),
    path('makeProjectComment/<int:pk>', views.makeProjectComment, name='makeProjectComment'),
]