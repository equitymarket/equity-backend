# -*- coding:utf-8 -*-

from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .models import Strategy
from .serializers import StrategySerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@api_view(['GET'])
def strategy_list(request):
    """
    list all strategy，return all information

    Author:

    Args:

    Returns:
        :

    Raises:
        ValueError:
    """

    output = Strategy.objects.all()
    serializer = StrategySerializer(output, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def strategy_totolreturn(request):
    """
    list all strategy，return base information,filted by totolreturn

    Author:

    Args:

    Returns:
        :

    Raises:
        ValueError:
    """

    output = Strategy.objects.values("name","price","maxwithdraw","totalreturn", "todayreturn",).order_by("-totalreturn")
    serializer = StrategySerializer(output, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def strategy_maxwithdraw(request):
    """
    list all strategy，return base information,filted by maxwithdraw

    Author:

    Args:

    Returns:
        :

    Raises:
        ValueError:
    """

    output = Strategy.objects.values("name","price","maxwithdraw","totalreturn", "todayreturn",).order_by("-maxwithdraw")
    serializer = StrategySerializer(output, many=True)
    return Response(serializer.data)
