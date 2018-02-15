# -*- coding:utf-8 -*-

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Strategy, StrategySerializer


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

    output = Strategy.objects.values("name", "price", "maxwithdraw", "totalreturn", "todayreturn", ).order_by(
        "-totalreturn")
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

    output = Strategy.objects.values("name", "price", "maxwithdraw", "totalreturn", "todayreturn", ).order_by(
        "-maxwithdraw")
    serializer = StrategySerializer(output, many=True)
    return Response(serializer.data)
