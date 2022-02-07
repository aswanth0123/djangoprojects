"""bikerentalsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from.import views

urlpatterns = [
    path('',views.home,name='home'),

    path('h',views.home,name='home'),
    path('cbike',views.log,name='log'),
    path('contact',views.contact,name='contact'),
    path('help',views.help,name='help'),
    path('cprofile',views.customerprofile,name='customerprofile'),
    path('customerbike',views.bike,name='bike'),
    path('reg',views.cregister,name='cregister'),
    path('log',views.log,name='log'),
    path('login2',views.log,name='log'),
    path('register',views.cregister,name='cregister'),
    path('adreg',views.adregister,name='adregister'),

    path('adboard',views.adboard,name='adboard'),
    path('bike',views.bike,name='bike'),

    #admin dashboard
    path('cdetails',views.cdetails,name='cdetails'),
    path('bdetails',views.bdetails,name='bdetails'),
    path('bookdetails',views.bookdetails,name='bookdetails'),
    path('addbike',views.addbike,name='addbike'),
    path('changepassword',views.changepassword,name='changepassword'),

    path('addingbike',views.addingbike,name='addingbike'),
    path('edit',views.edit,name='edit'),
    path('delete',views.delete,name='delete'),
    path('delete1',views.delete1,name='delete1'),


    path('login',views.login1,name='login1'),
    path('logout',views.logout,name='logout'),
    path('logout1',views.logout,name='logout'),
    path('cregistration',views.cregistration,name='cregistration'),
    path('addingbike',views.addingbike,name='addingbike'),

]
