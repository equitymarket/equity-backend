# -*- coding:utf-8 -*-

from app import views
from django.conf.urls import url, include
urlpatterns = [
    url(r'permissions/list$', views.permissions_list),
    url(r'users/list$', views.users_list),
]