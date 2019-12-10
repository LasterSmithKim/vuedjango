"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
import xadmin
#配置图片显示路径
from MxShop.settings import MEDIA_ROOT
from django.views.static import serve
#drf文档
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from goods.views import GoodsListViewSet, CategoryViewSet
router = DefaultRouter()
#配置goods的url
router.register(r'goods', GoodsListViewSet)
router.register(r'category', CategoryViewSet)
#from goods.views import GoodsListView
#token身份验证url请求入口
from rest_framework.authtoken import views
#jwt的身份验证模块
from rest_framework_jwt.views import obtain_jwt_token



urlpatterns = [
    #path(r'admin/', admin.site.urls),
    path(r'xadmin/', xadmin.site.urls),
    path(r'ueditor/', include('DjangoUeditor.urls')),
    # 文件 图片
    path(r'media/<path:path>', serve, {'document_root': MEDIA_ROOT}),
    #drf文档，title自定义
    path(r'docs',include_docs_urls(title='django + vue')),
    #drf 登录入口
    path(r'api-auth/',include('rest_framework.urls', namespace='rest_framework')),
    #path(r'goods/', GoodsListView.as_view(), name='goods-list')
    # token身份验证url请求入口
    path(r'api-token-auth/', views.obtain_auth_token),
    #jwt的身份验证模块url请求入口
    path(r'login/', obtain_jwt_token),
    re_path('^', include(router.urls)),

]
