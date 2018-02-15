# -*- coding:utf-8 -*-

from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Strategy


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class StrategySerializer(serializers.ModelSerializer):
    class Meta:
        model = Strategy
        fields = ('id', 'name', 'created', 'updated', 'price', 'pricipal',
                  'level', 'subscription', 'purchase', 'maxwithdraw', 'totalreturn', 'todayreturn', 'classification',)
