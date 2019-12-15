from django.shortcuts import render
from rest_framework import mixins, viewsets
from .models import UserFav
from .serializers import UserFavSerializer
# Create your views here.


class UserFavViewset(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    '''
    用户收藏
    '''
    queryset = UserFav.objects.all()
    serializer_class = UserFavSerializer

