from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from utils.permissions import IsOwnerOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from .models import UserFav
from .serializers import UserFavSerializer
# Create your views here.


class UserFavViewset(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin):
    '''
    用户收藏
    '''
    #queryset = UserFav.objects.all()
    #permission是用来做权限判断的
    # IsAuthenticated：必须登录用户；IsOwnerOrReadOnly：必须是当前登录的用户
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    serializer_class = UserFavSerializer
    #auth使用来做用户认证的
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    # 搜索的字段
    lookup_field = "goods_id"

    def get_queryset(self):
        #只能查看当前登录用户的收藏，不会获取所有用户的收藏
        return UserFav.objects.filter(user=self.request.user)

