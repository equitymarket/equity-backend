# -*- coding:utf-8 -*-

import hashlib

from django.db import models
from rest_framework import serializers


class AppUser(models.Model):
    """用户表"""
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    mobile = models.CharField(max_length=30)
    wechat = models.CharField(max_length=30, null=True, default=None)
    alipay = models.CharField(max_length=30, null=True)
    rank = models.IntegerField(default=1)  # 用户等级 1-普通用户
    points = models.IntegerField(default=0)  # 积分
    invitecode = models.CharField(max_length=30, null=True)
    role = models.ForeignKey(to='Role', default=1)
    openid = models.CharField(max_length=100, null=True)
    unionid = models.CharField(max_length=100, null=True)  # 跨公众号的unionid
    officialaccount = models.IntegerField(default=1)  # 公众号编码 不排除创建多个公众号
    refresh_token = models.CharField(max_length=512, null=True)  # 刷新的token
    created = models.DateField(auto_now_add=True)  # 创建时间
    updated = models.DateField(auto_now_add=True)  # 更新时间

    def __str__(self):
        return self.name

    def is_authenticated(self):
        return True

    def hashed_password(self, password=None):
        if not password:
            return self.password
        else:
            return hashlib.md5(password).hexdigest()

    def check_password(self, password):
        if self.hashed_password(password) == self.password:
            return True
        return False


class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ('name', 'password', 'mobile', 'wechat', 'alipay', 'rank', 'points', 'invitecode', 'role',
                  'openid', 'unionid', 'officialaccount', 'refresh_token')


class Role(models.Model):
    """用户角色表"""
    name = models.CharField(max_length=30, unique=True)
    permission = models.ManyToManyField(to='Permission')
    created = models.DateField(auto_now_add=True)  # 创建时间
    updated = models.DateField(auto_now_add=True)  # 更新时间

    def __str__(self):
        return self.name


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('name', 'permission')


class Permission(models.Model):
    """权限表"""
    name = models.CharField(max_length=30, unique=True, default=None)
    created = models.DateField(auto_now_add=True)  # 创建时间
    updated = models.DateField(auto_now_add=True)  # 更新时间

    def __str__(self):
        return self.name


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('id', 'name')


class Mytrade(models.Model):
    """用户自主交易记录表"""
    appuser = models.ForeignKey(to='AppUser')
    code = models.CharField(max_length=10, null=True)  # 股票代码
    direction = models.IntegerField(default=1)  # 交易方向 1-买入 2-卖出
    created = models.DateField(auto_now_add=True)  # 创建时间
    updated = models.DateField(auto_now_add=True)  # 更新时间
    price = models.DecimalField(max_digits=10, decimal_places=3, null=True)  # 成交价
    volume = models.DecimalField(max_digits=10, decimal_places=3, null=True)  # 成交量
    dealtype = models.ForeignKey(to='DealType', default=1)  # 交易类型

    def __str__(self):
        return self.code


class MytradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mytrade
        fields = ('appuser', 'code', 'direction', 'created', 'price', 'volume', 'dealtype')


class StrategySerializer(serializers.ModelSerializer):
    class Meta:
        model = Strategy
        fields = ('name', 'price', 'principal', 'created', 'updated', 'level', 'subscription', 'purchase',
                  'maxwithdraw', 'totalreturn', 'todayreturn', 'strategyclassification', 'appusers')


class BuyRecord(models.Model):
    """交易策略购买记录，包含未购买"""
    appuser = models.ForeignKey(to=AppUser)
    strategy = models.ForeignKey(to=Strategy)
    status = models.IntegerField(default=1)  # 购买状态 1-已购买 2-已加入购物车
    created = models.DateField(auto_now_add=True)  # 创建时间
    updated = models.DateField(auto_now_add=True)  # 更新时间

    def __str__(self):
        return self.appuser + ':' + self.strategy


class BuyRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyRecord
        fields = ('appuser', 'strategy', 'status', 'created')


class StrategyClassification(models.Model):
    """策略分类表"""
    name = models.CharField(max_length=30, unique=True)
    created = models.DateField(auto_now_add=True)  # 创建时间
    updated = models.DateField(auto_now_add=True)  # 更新时间

    def __str__(self):
        return self.name


class StrategyClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyRecord
        fields = ('appuser', 'strategy', 'status', 'created')


class Trade(models.Model):
    """策略交易历史记录"""
    strategy = models.ForeignKey(to='Strategy')
    code = models.CharField(max_length=10)  # 股票代码
    direction = models.IntegerField()  # 交易方向
    created = models.DateField(auto_now_add=True)  # 创建时间
    price = models.DecimalField(max_digits=10, decimal_places=3)  # 成交价
    volume = models.DecimalField(max_digits=10, decimal_places=3)  # 成交量
    dealtype = models.ForeignKey(to='DealType')  # 交易类型


class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = ('strategy', 'code', 'direction', 'created', 'price', 'volume', 'dealtype')


class DealType(models.Model):
    """交易类型"""
    name = models.CharField(max_length=30, default='限价单', unique=True)  # 类型名称
    created = models.DateField(auto_now_add=True)  # 创建时间
    # 其它交易类型的基础信息


class DealTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealType
        fields = ('name',)


class Stock(models.Model):
    """股票基础信息表"""
    name = models.CharField(max_length=30)  # 股票名称
    code = models.CharField(max_length=10, unique=True, null=False)  # 股票代码


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('name', 'code')


class Strategy(models.Model):
    name = models.CharField('策略名称', max_length=50)
    price = models.DecimalField('成交价', max_digits=12, decimal_places=2, null=True)
    pricipal = models.DecimalField('本金', max_digits=12, decimal_places=2, null=True)
    created = models.DateField('创建时间', auto_now_add=True)
    updated = models.DateTimeField('更新时间', auto_now=True)
    level = models.IntegerField('策略级别', default=1)
    subscription = models.IntegerField('订阅数量', default=0)
    purchase = models.IntegerField('购买量', default=0)
    maxwithdraw = models.DecimalField('最大回撤,百分比率', max_digits=5, decimal_places=4, null=True)
    totalreturn = models.DecimalField('累计收益，百分比率', max_digits=5, decimal_places=4, null=True)
    todayreturn = models.DecimalField('今日收益，百分比率', max_digits=5, decimal_places=4, null=True)
    classification = models.IntegerField('策略类别', default=1)
    appusers = models.ManyToManyField(AppUser, through='BuyRecord')  # 购买的用户

    def __str__(self):
        return self.name
