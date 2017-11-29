# -*- coding:utf-8 -*-

from rest_framework import serializers
from .models import Strategy


class StrategySerializer(serializers.ModelSerializer):
    class Meta:
        model = Strategy
        fields = ('id', 'name', 'created','updated', 'price','pricipal',
                 'level','subscription','purchase','maxwithdraw','totalreturn', 'todayreturn', 'classification',)
