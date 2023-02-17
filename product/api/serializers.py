from rest_framework import serializers
from product.models import Product, Product_version, Category, Manufacturer, Color

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category 
        fields = [
            'id',
            'name',
            'is_navbar',
            'p_category'
        ]

class ManufacturerReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacturer
        fields = [
            'name'
        ]

class ColorReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = [
            'name'
        ]

class ProductReadSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    detail_url = serializers.SerializerMethodField()
    manufacturer = ManufacturerReadSerializer()
    
    class Meta:
        model = Product 
        fields = [
            'id', 
            'name', 
            'overview',
            'price', 
            'in_sale',
            'discount', 
            'new_price',
            'manufacturer',
            'details', 
            'category',
            'detail_url'
        ]

    def get_detail_url(self, obj):
        return obj.get_absolute_url()

class ProductVersionSerializer(serializers.ModelSerializer):
    product = ProductReadSerializer()
    color = ColorReadSerializer()

    class Meta:
        model = Product_version
        fields = [
            'id', 
            'color',
            'cover_image',
            'product',
            'quantity',
            'review_count',
            'read_count'
        ]