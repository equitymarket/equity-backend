#-*- coding:utf-8 -*-

from django.http import *
from .models import *
from equity.config import wechat
import requests
from django.core.cache import cache
from django.contrib.auth.decorators import login_required


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
def hello_world(request):
    data = {
        'a': 1,
        'b': 2,
    }
    return JsonResponse(data)


def test_login(request):
    """用户登陆"""
    return JsonResponse({'success': True, 'msg': '登陆页'})


def permissions_list(request):
    """权限列表"""
    l = PermissionSerializer(Permission.objects.all(), many=True)
    return JsonResponse(l.data, safe=False)


def users_list(request):
    """用户列表"""
    users = User.objects.all()
    l = UserSerializer(User.objects.all(), many=True)
    return JsonResponse(l.data, safe=False)
