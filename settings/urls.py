"""
URL configuration for settings project.

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
from web_bank import views
from web_bank.views import *

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.index, name='index'),
    path('reg/', RegisterUser.as_view(), name='reg'),
    path('login/', LoginUser.as_view(), name='login'),
    path('famous-clients/', Persons.as_view(), name='clients'),
    path('products/', products, name='products', kwargs={'id': 0}),
    path('products/<int:id>/', products, name='products',),
]
