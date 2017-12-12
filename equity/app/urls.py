# -*- coding:utf-8 -*-

from app import views
from django.conf.urls import url, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'strategies', views.StrategyVeiwSet)
router.register(r'buyrecords', views.BuyRecordsViewSet)
router.register(r'trades', views.TradeVeiwSet)

urlpatterns = [
    # url(r'permissions/list$', views.permissions_list),
    # url(r'users/list$', views.users_list),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]