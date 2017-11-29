# -*- coding:utf-8 -*-
from django.conf.urls import  url
from . import views

urlpatterns = [
    url(r'strategy/list/$', views.strategy_list, name='strategy_list'),
    url(r'strategy/totolreturn$', views.strategy_totolreturn, name='strategy_totolreturn'),
    url(r'strategy/maxwithdraw$', views.strategy_maxwithdraw, name='strategy_maxwithdraw'),
]
