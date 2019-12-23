from rest_framework import serializers
from goods.models import Goods
from .models import ShoppingCart
from goods.serializers import GoodsSerializer

class ShopCartDetailSerializer(serializers.ModelSerializer):
    '''
        购物车商品详情信息
        '''
    # 一个购物车对应一个商品
    goods = GoodsSerializer(many=False, read_only=True)

    class Meta:
        model = ShoppingCart
        fields = "__all__"

class ShopCartSerializer(serializers.Serializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    nums = serializers.IntegerField(required=True, label='数量', min_value=1,
                                         error_messages={
                                             'required':'请选择商品数量',
                                             'min_value':'最小数量不能小于1'
                                         })
    goods = serializers.PrimaryKeyRelatedField(required=True, queryset=Goods.objects.all())

    def create(self, validated_data):
        user = self.context["request"].user
        nums = validated_data['nums']
        goods = validated_data['goods']

        existed = ShoppingCart.objects.filter(user=user, goods=goods)

        if existed:
            existed = existed[0]
            existed.nums += nums
            existed.save()
        else:
            existed = ShoppingCart.objects.create(**validated_data)
        return existed

    def update(self, instance, validated_data):
        # 修改商品数量
        instance.nums = validated_data["nums"]
        instance.save()
        return instance