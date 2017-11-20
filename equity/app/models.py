from django.db import models


# Create your models here.
class User(models.Model):
    """用户表"""
    name = models.CharField(max_length=30, default=None)
    password = models.CharField(max_length=30, default=None)
    mobile = models.CharField(max_length=30, default=None)
    wechat = models.CharField(max_length=30, default=None)
    alipay = models.CharField(max_length=30, default=None)
    rank = models.IntegerField(default=1)  # 用户等级 1-普通用户
    points = models.IntegerField(default=0)  # 积分
    invitecode = models.CharField(max_length=30, default=None)
    role = models.ForeignKey(to='Role')


class Role(models.Model):
    """用户角色表"""
    name = models.CharField(max_length=30, unique=True)
    permission = models.ManyToManyField(to='Permission')


class Permission(models.Model):
    """权限表"""
    pass


class Mytrade(models.Model):
    """用户自主交易记录表"""
    id_user = models.ForeignKey(to='User')


class Stratedy(models.Model):
    """交易策略表"""
    name = models.CharField(max_length=30, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    pricipal = models.DecimalField(max_digits=10, decimal_places=3)  # 本金
    created = models.DateField(auto_now=True)  # 创建时间
    updated = models.DateField(auto_now=True)  # 更新时间
    level = models.IntegerField(default=1)  # 1-初级免费 2-中级  。。。 待完善
    subscription = models.IntegerField(default=0)  # 订阅量
    purchase = models.IntegerField(default=0)  # 购买量
    maxwithdraw = models.DecimalField(max_digits=10, decimal_places=3)  # 最大回撤
    totalreturn = models.DecimalField(max_digits=10, decimal_places=3)  # 累计收益
    todayreturn = models.DecimalField(max_digits=10, decimal_places=3)  # 今日收益
    stratedyclassification = models.ForeignKey(to='StratedyClassification')  # 策略类别
    users = models.ManyToManyField(User, through='BuyRecord')


class BuyRecord(models.Model):
    """交易策略购买记录，包含未购买"""
    user = models.ForeignKey(to=User)
    stratedy = models.ForeignKey(to=Stratedy)
    status = models.IntegerField(default=1)  # 购买状态 1-已购买 2-已加入购物车
    created = models.DateField(auto_now=True)  # 创建时间


class StratedyClassification(models.Model):
    """策略分类表"""
    name = models.CharField(max_length=30, unique=True)


class Trade(models.Model):
    """策略交易历史记录"""
    id_Stratedy = models.ForeignKey(to='Stratedy')
    code = models.CharField(max_length=10)  # 股票代码
    direction = models.IntegerField()  # 交易方向
    created = models.DateField(auto_now=True)  # 创建时间
    price = models.DecimalField(max_digits=10, decimal_places=3)  # 成交价
    volume = models.DecimalField(max_digits=10, decimal_places=3)  # 成交量
    dealtype = models.ForeignKey(to='DealType')  # 交易类型


class DealType(models.Model):
    """交易类型"""
    name = models.CharField(max_length=30, default=30, unique=True)  # 类型名称
    # 其它交易类型的基础信息


class Stock(models.Model):
    """股票基础信息表"""
    name = models.CharField(max_length=30)  # 股票名称
    code = models.CharField(max_length=10, unique=True, null=False)  # 股票代码
