from rest_framework import serializers
from .models import Goods, GoodsCategory, GoodsImage



class GoodsCategorySerializer3(serializers.ModelSerializer):
    '''三级分类'''
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsCategorySerializer2(serializers.ModelSerializer):
    '''
    二级分类
    '''
    #在parent_category字段中定义的related_name="sub_cat"
    sub_cat = GoodsCategorySerializer3(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"


    #商品分类
class GoodsCategorySerializer(serializers.ModelSerializer):
    """
    商品一级类别序列化
    """
    sub_cat = GoodsCategorySerializer2(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"


#轮播图
class GoodsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsImage
        fields = ("image",)

class GoodsSerializer(serializers.ModelSerializer): #参数serializers.Serializer
    #name = serializers.CharField(max_length=100, required=True)
    #click_num = serializers.IntegerField(default=0)
    #goods_front_image = serializers.ImageField()
    category = GoodsCategorySerializer() #外键的 序列化 嵌套
    # images是数据库中设置的related_name="images"
    images = GoodsImageSerializer(many=True)
    class Meta:
        model = Goods
        #fields = ('name', 'click_num', 'market_price', 'add_time')
        fields = "__all__"

    def create(self, validated_data):
        """
        Create and return a new Good instance, give the validated data
        :param validated_data:
        :return:
        """
        return Goods.objects.create(**validated_data)


