from django.shortcuts import render

from rest_framework.views import APIView
from goods.serializers import GoodsSerializer
from rest_framework.response import Response
from rest_framework import status

from .models import Goods
# Create your views here.

class GoodsListView(APIView):
    """
    List all goods, or create a new good.
    """
    def get(self, request, format=None):
        goods = Goods.objects.all()[:100]
        goods_serializer = GoodsSerializer(goods, many=True)
        return Response(goods_serializer.data)

    def post(self, request):
        serializer = GoodsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

