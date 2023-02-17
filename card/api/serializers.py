from rest_framework import serializers
from product.api.serializers import ProductVersionSerializer
from card.models import wishlist,basket,basket_item

class WishlistSerializer(serializers.ModelSerializer):
    product = ProductVersionSerializer(many=True)

    class Meta:
        model = wishlist
        fields = [
            'user',
            'product'
        ]


class BasketSerializer(serializers.ModelSerializer):

    class Meta:
        model = basket
        fields = [
            'user',
            'items',
            'is_active'
        ]

class BasketItemSerializer(serializers.ModelSerializer):
    product = ProductVersionSerializer()

    class Meta:
        model = basket_item
        fields = ['user', 'product', 'quantity']







