# -*- coding:utf-8 -*-

from app import api
from app import views
from django.conf.urls import url, include

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'strategies', views.StrategyVeiwSet)
router.register(r'buyrecords', views.BuyRecordsViewSet)
router.register(r'trades', views.TradeVeiwSet)

urlpatterns = [
    # 用户
    url(r'api/wx/users/create$', views.create_user),
    url(r'api/wx/users/update$', views.update_user),
    url(r'api/wx/users/delete', views.delete_user),
    url(r'api/wx/users/detail/(?P<user_id>[0-9]+)$', views.get_user_detail),
    url(r'api/wx/users/list$', views.get_users),
    # 权限
    url(r'api/wx/permissions/create$', views.create_permission),
    url(r'api/wx/permissions/update$', views.update_permission),
    url(r'api/wx/permissions/delete', views.delete_permission),
    url(r'api/wx/permissions/detail/(?P<user_id>[0-9]+)$', views.get_permission_detail),
    url(r'api/wx/permissions/list$', views.get_permissions),
    # 角色
    url(r'api/wx/roles/create$', views.create_role),
    url(r'api/wx/roles/update$', views.update_role),
    url(r'api/wx/roles/delete', views.delete_role),
    url(r'api/wx/roles/detail/(?P<user_id>[0-9]+)$', views.get_role_detail),
    url(r'api/wx/roles/list$', views.get_roles),
    # 策略
    url(r'api/wx/strategies/create$', views.create_strategy),
    url(r'api/wx/strategies/update$', views.update_strategy),
    url(r'api/wx/strategies/delete', views.delete_strategy),
    url(r'api/wx/strategies/detail/(?P<user_id>[0-9]+)$', views.get_strategy_detail),
    url(r'api/wx/strategies/list$', views.get_strategies),





    url(r'strategy/list/$', api.strategy_list, name='strategy_list'),
    url(r'strategy/totolreturn$', api.strategy_totolreturn, name='strategy_totolreturn'),
    url(r'strategy/maxwithdraw$', api.strategy_maxwithdraw, name='strategy_maxwithdraw'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]