# from rest_framework import serializers
# from .models import Product, Category
# from apps.user.serializers import UserSerializer
#
#
# class CategorySerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Category
#         fields = "__all__"
#
#
# class ProductSerializer(serializers.ModelSerializer):
#     seller = UserSerializer()
#     category = CategorySerializer()
#
#     class Meta:
#         model = Product
#         fields = "__all__"
import logging

from rest_framework import serializers
from .models import Product
from apps.user.serializers import UserSerializer
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    seller = UserSerializer()
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = "__all__"

    def update(self, instance, validated_data):
        logging.info(f'Trying to update product with data: {validated_data}')

        validated_data.pop('seller', True)
        validated_data.pop('category', None)

        try:
            # Perform the default update for other fields
            result = super().update(instance, validated_data)
            logging.info(f'Product updated successfully: {result}')
            return result
        except Exception as e:
            logging.error(f'Error updating product: {e}')
            raise serializers.ValidationError(f'Error updating product: {e}')
