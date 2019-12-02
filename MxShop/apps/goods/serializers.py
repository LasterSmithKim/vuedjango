from rest_framework import serializers
from .models import Goods, GoodsCategory

class GoodsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer): #参数serializers.Serializer
    #name = serializers.CharField(max_length=100, required=True)
    #click_num = serializers.IntegerField(default=0)
    #goods_front_image = serializers.ImageField()
    category = GoodsCategorySerializer() #外键的 序列化 嵌套
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