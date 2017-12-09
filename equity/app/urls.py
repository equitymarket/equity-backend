# -*- coding:utf-8 -*-

import api
import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'permissions/list$', views.permissions_list),
    url(r'users/list$', views.users_list),
    url(r'strategy/list/$', api.strategy_list, name='strategy_list'),
    url(r'strategy/totolreturn$', api.strategy_totolreturn, name='strategy_totolreturn'),
    url(r'strategy/maxwithdraw$', api.strategy_maxwithdraw, name='strategy_maxwithdraw'),
]