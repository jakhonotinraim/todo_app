"""todo_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from todos.views import delete, home, about, create_todo, completed, delete, todo_api, todo_detail 
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('create_todo/', create_todo, name='create-todo'),
    path('completed/<int:pk>/', completed, name='completed'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('todo_rest/', todo_api),
    path('todo_rest/<int:id>', todo_detail),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns = format_suffix_patterns(urlpatterns)

