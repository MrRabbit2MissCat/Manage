"""Manage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from index.views import things_in, index, show, excel_upload, manage, search, manage_search, delete, change, edit, \
    warehouse, show_warehouse, search_ware, warehousein, delete_ware, change_ware, edit_ware
from login.views import login, do_login, register, do_register
from treatdata.views import treat_data, show_data, search_data

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/',login),
    path('do_login/',do_login),

    path('register/',register),
    path('do_register/',do_register),

    path('index/',index),
    path('things_in/',things_in),
    path('excel_upload/',excel_upload),

    path('show/',show),
    path('search/',search),

    path('manage/',manage),
    path('manage_search/',manage_search),
    path('del/',delete),
    path('change/',change),
    path('edit/',edit),

    path('treat/',treat_data),
    path('show_data/',show_data),
    path('search_data/',search_data),

    path('warehouse/',warehouse),
    path('show_warehouse/',show_warehouse),
    path('search_ware/', search_ware),
    path('warehousein/', warehousein),
    path('del_ware/',delete_ware),
    path('change_ware/',change_ware),
    path('edit_ware/',edit_ware)
]
