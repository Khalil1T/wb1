from rest_framework import serializers
from .models import Product, Category
from apps.user.models import User
from apps.user.serializers import UserSerializer
from rest_framework import permissions, status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id','name']
class ProductSerializer(serializers.ModelSerializer):
    serializer_user = UserSerializer
    serializer_category = CategorySerializer
    class Meta:
        model = Product
        fields = "__all__"


class ProductSerializer_NotAll(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['name','description','price','quantity']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['name', 'email']
class CombinedSerializer(serializers.Serializer):
    product_data = ProductSerializer_NotAll(many=True)
    category_data = CategorySerializer(many=True)
