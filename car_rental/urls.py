"""
URL configuration for car_rental project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

from django.contrib import admin 
from django.urls import path 
from django.conf.urls.static import static 
from django.conf import  settings 


from .views import index
from .views import login
from .views import about
from .views import main
from .views import book
from .views import sample
from .views import register,cars

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('login/',login,name='login'),
    path('about/',about,name='about'),
    path('',main,name='main'),
    path('book/',book,name='book'),
    path('sample/',sample,name='sample'), 
    path('register/',register,name='register'),
     path('cars/',cars,name='cars'),
]