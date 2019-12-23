from rest_framework import serializers
from goods.models import Goods
from .models import ShoppingCart



class ShopCartSerializer(serializers.Serializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    goods_num = serializers.IntegerField(required=True, label='数量', min_value=1,
                                         error_messages={
                                             'required':'请选择商品数量',
                                             'min_value':'最小数量不能小于1'
                                         })
    goods = serializers.PrimaryKeyRelatedField(required=True, queryset=Goods.objects.all())

    def create(self, validated_data):
        user = self.context["request"].user
        goods_num = validated_data['goods_num']
        goods = validated_data['goods']

        existed = ShoppingCart.objects.filter(user=user, goods=goods)

        if existed:
            existed = existed[0]
            existed.goods_num += goods_num
            existed.save()
        else:
            existed = ShoppingCart.objects.create(**validated_data)
        return existed

    def update(self, instance, validated_data):
        # 修改商品数量
        instance.goods_num = validated_data["goods_num"]
        instance.save()
        return instance