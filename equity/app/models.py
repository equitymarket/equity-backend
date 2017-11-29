#-*- coding:utf-8 -*-

from django.db import models


class Strategy(models.Model):
    name = models.CharField('策略名称',max_length=50)
    price = models.DecimalField('成交价',max_digits=12, decimal_places=2, null=True)
    pricipal = models.DecimalField('本金',max_digits=12, decimal_places=2, null=True)
    created = models.DateField('创建时间',auto_now_add=True)
    updated = models.DateTimeField('更新时间',auto_now=True)
    level = models.IntegerField('策略级别',default=1)
    subscription = models.IntegerField('订阅数量',default=0)
    purchase = models.IntegerField('购买量',default=0)
    maxwithdraw = models.DecimalField('最大回撤,百分比率',max_digits=5, decimal_places=4, null=True)
    totalreturn = models.DecimalField('累计收益，百分比率',max_digits=5, decimal_places=4, null=True)
    todayreturn = models.DecimalField('今日收益，百分比率',max_digits=5, decimal_places=4, null=True)
    classification = models.IntegerField('策略类别',default=1)

    def __unicode__(self):
        return self.name


