from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from utils.permissions import IsOwnerOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from .models import UserFav
from .serializers import UserFavSerializer
# Create your views here.


class UserFavViewset(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    '''
    用户收藏
    '''
    #queryset = UserFav.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    serializer_class = UserFavSerializer
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_queryset(self):
        #只能查看当前登录用户的收藏，不会获取所有用户的收藏
        return UserFav.objects.filter(user=self.request.user)

