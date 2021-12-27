from rest_framework import serializers

from ..models import Category, ProductRange, Product


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ProductRangeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductRange
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):

    product_range = ProductRangeSerializer()

    class Meta:
        model = Product
        fields = '__all__'





