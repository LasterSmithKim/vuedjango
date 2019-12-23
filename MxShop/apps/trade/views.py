from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from utils.permissions import IsOwnerOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from .serializers import ShopCartSerializer
from .models import ShoppingCart

# Create your views here.


class ShopingCartViewset(viewsets.ModelViewSet):
    '''
    购物车功能
    list:
        获取购物车详情
    create:
        加入购物车
    delete:
        删除购物车
    update:
        更新购物车
    '''

    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = ShopCartSerializer
    #queryset = ShoppingCart.objects.all()

    lookup_field = "goods_id"

    # 获取购物车列表
    def get_queryset(self):
        return ShoppingCart.objects.filter(user=self.request.user)