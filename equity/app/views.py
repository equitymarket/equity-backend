# -*- coding:utf-8 -*-

from django.contrib.auth.models import User
from django.http import *
from app.models import *
from app.serializers import UserSerializer
from equity.config import wechat
import requests
from django.core.cache import cache
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.decorators import api_view


@api_view(['POST'])
def create_user(request):
    print(request.data)
    # todo: create user
    # user = AppUser(request.data)
    # user.save()
    return JsonResponse({'status': '0', 'msg': 'success', 'data': request.data})


@api_view(['POST'])
def update_user(request):
    print(request.data)
    # todo: update user
    # AppUser.objects.update()
    return JsonResponse({'status': '0', 'msg': 'success', 'data': request.data})


@api_view(['POST'])
def delete_user(request):
    print(request.data)
    # todo: delete user
    # AppUser.objects.update()
    return JsonResponse({'status': '0', 'msg': 'success', 'data': request.data})


@api_view(['GET'])
def get_user_detail(request, user_id):
    print(user_id)
    # todo: get user detail
    detail = {}
    # detail = AppUser.objects.get(user_id)
    return JsonResponse({'status': '0', 'msg': 'success', 'data': detail})


@api_view(['GET'])
def get_users(request):
    # todo: get user list by filter
    qs = request.query_params
    # AppUser.objects.find()
    users = [{}, {}]
    return JsonResponse({'status': '0', 'msg': 'success', 'data': users})


@api_view(['POST'])
def create_permission(request):
    print(request.data)
    # todo: create permission
    # user = AppUser(request.data)
    # user.save()
    return JsonResponse({'status': '0', 'msg': 'success', 'data': request.data})


@api_view(['POST'])
def update_permission(request):
    print(request.data)
    # todo: update permission
    # AppUser.objects.update()
    return JsonResponse({'status': '0', 'msg': 'success', 'data': request.data})


@api_view(['POST'])
def delete_permission(request):
    print(request.data)
    # todo: delete permission
    # AppUser.objects.update()
    return JsonResponse({'status': '0', 'msg': 'success', 'data': request.data})


@api_view(['GET'])
def get_permission_detail(request, permission_id):
    print(permission_id)
    # todo: get permission detail
    detail = {}
    # detail = AppUser.objects.get(user_id)
    return JsonResponse({'status': '0', 'msg': 'success', 'data': detail})


@api_view(['GET'])
def get_permissions(request):
    # todo: get permission list by filter
    qs = request.query_params
    # AppUser.objects.find()
    permissions = [{}, {}]
    return JsonResponse({'status': '0', 'msg': 'success', 'data': permissions})


@api_view(['POST'])
def create_role(request):
    print(request.data)
    # todo: create role
    # role = Role(request.data)
    # role.save()
    return JsonResponse({'status': '0', 'msg': 'success', 'data': request.data})


@api_view(['POST'])
def update_role(request):
    print(request.data)
    # todo: update role
    # AppUser.objects.update()
    return JsonResponse({'status': '0', 'msg': 'success', 'data': request.data})


@api_view(['POST'])
def delete_role(request):
    print(request.data)
    # todo: delete role
    # AppUser.objects.update()
    return JsonResponse({'status': '0', 'msg': 'success', 'data': request.data})


@api_view(['GET'])
def get_role_detail(request, role_id):
    print(role_id)
    # todo: get permission detail
    detail = {}
    # detail = AppUser.objects.get(user_id)
    return JsonResponse({'status': '0', 'msg': 'success', 'data': detail})


@api_view(['GET'])
def get_roles(request):
    # todo: get role list by filter
    qs = request.query_params
    # AppUser.objects.find()
    roles = [{}, {}]
    return JsonResponse({'status': '0', 'msg': 'success', 'data': roles})


@api_view(['POST'])
def create_strategy(request):
    print(request.data)
    # todo: create strategy
    # strategy = Strategy(request.data)
    # strategy.save()
    return JsonResponse({'status': '0', 'msg': 'success', 'data': request.data})


@api_view(['POST'])
def update_strategy(request):
    print(request.data)
    # todo: update strategy
    # Strategy.objects.update()
    return JsonResponse({'status': '0', 'msg': 'success', 'data': request.data})


@api_view(['POST'])
def delete_strategy(request):
    print(request.data)
    # todo: delete strategy
    # AppUser.objects.update()
    return JsonResponse({'status': '0', 'msg': 'success', 'data': request.data})


@api_view(['GET'])
def get_strategy_detail(request, role_id):
    print(role_id)
    # todo: get strategy detail
    detail = {}
    # detail = AppUser.objects.get(user_id)
    return JsonResponse({'status': '0', 'msg': 'success', 'data': detail})


@api_view(['GET'])
def get_strategies(request):
    # todo: get strategy list by filter
    qs = request.query_params
    # AppUser.objects.find()
    strategies = [{}, {}]
    return JsonResponse({'status': '0', 'msg': 'success', 'data': strategies})





# 微信授权相关
def wechat_login(request):
    """微信授权登陆"""
    params = request.GET.copy()
    code = params.get('code')
    state = params.get('state')
    qs = {
        'appid': wechat['appid'],
        'secret': wechat['appsecret'],
        'code': code,
        'grant_type': 'authorization_code',
    }
    url = 'https://api.weixin.qq.com/sns/oauth2/access_token'
    res = requests.get(url, qs)
    data = res.content
    # {"access_token": "ACCESS_TOKEN",
    # "expires_in": 7200,
    # "refresh_token": "REFRESH_TOKEN",
    # "openid": "OPENID",
    # "scope": "SCOPE"}
    access_token = data.get('access_token')
    expires_in = data.get('expires_in')
    refresh_token = data.get('refresh_token')
    openid = data.get('openid')
    scope = data.get('scope')
    errcode = data.get('errcode')
    if not errcode:  # 返回成功
        cache.set(access_token, openid, expires_in)  # 入库
        cache.set(refresh_token, openid, 30 * 24 * 60 * 60)  # 刷新的token
    else:  # 返回失败
        pass

    # 寻找access_token
    # 当无法找到access_token, 刷新access_token
    # ?appid=APPID&grant_type=refresh_token&refresh_token=REFRESH_TOKEN
    qs2 = {
        'appid': wechat['appid'],
        'refresh_token': refresh_token,
        'grant_type': 'refresh_token',
    }
    refresh_url = 'https://api.weixin.qq.com/sns/oauth2/refresh_token'
    new_token_info = requests.get(refresh_url, qs2)


@login_required(login_url='/accounts/login')
def login(request):
    data = {
        'a': 1,
        'b': 2,
    }
    return JsonResponse(data)


# def permissions_list(request):
#     """权限列表"""
#     l = PermissionSerializer(Permission.objects.all(), many=True)
#     return JsonResponse(l.data, safe=False)


# def users_list(request):
#     """用户列表"""
#     users = User.objects.all()
#     l = UserSerializer(User.objects.all(), many=True)
#     return JsonResponse(l.data, safe=False)


def strategy_classification(request):
    """创建策略类别"""
    pass


class AppUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class StrategyVeiwSet(viewsets.ModelViewSet):
    """策略资源"""
    queryset = Strategy.objects.all().order_by('-created')
    serializer_class = StrategySerializer


class BuyRecordsViewSet(viewsets.ModelViewSet):
    """购买记录"""
    queryset = BuyRecord.objects.all().order_by('-created')
    serializer_class = BuyRecordSerializer


class TradeVeiwSet(viewsets.ModelViewSet):
    """交易记录"""
    queryset = Trade.objects.all().order_by('-created')
    serializer_class = TradeSerializer


class DealTypeViewSet(viewsets.ModelViewSet):
    """交易类型"""
    queryset = DealType.objects.all()
    serializer_class = DealTypeSerializer
