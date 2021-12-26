from rest_framework import serializers

from ..models import Categories,\
                    SubCategory,\
                    ProductTypeList,\
                    Product,\
                    ProductRange


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = '__all__'


class SubCategoriesSerializer(serializers.ModelSerializer):

    category = CategoriesSerializer()

    class Meta:
        model = SubCategory
        fields = '__all__'


class ProductTypeListSerializer(serializers.ModelSerializer):

    sub_category = SubCategoriesSerializer()

    class Meta:
        model = ProductTypeList
        fields = '__all__'






