# -*- coding:utf-8 -*-
"""通用方法"""

import requests
from equity.config import wechat


def get_access_token():
    # 从本地获取access_token
    # 如果获取不到则发请求到微信获取
    url = wechat['access_token_url']
    qs = {
        'grant_type': 'client_credential',
        'appid': wechat['appid'],
        'secret': wechat['appsecret'],
    }
    res = requests.get(url=url, params=qs)
    #  成功返回{"access_token": "ACCESS_TOKEN", "expires_in": 7200}
    #  错误返回 {"errcode":40013,"errmsg":"invalid appid"}
    # see https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1421140183
    data = res.content
    errcode = data.get('errcode')
    if not errcode or errcode == '0': # 返回成功
        pass
        access_token = data.get('access_token')
        expires_in = data.get('expires_in')  # 过期时间
        # 储存到redis或django自带缓存中
    else:
        print(data)