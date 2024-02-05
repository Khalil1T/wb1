from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, status, viewsets
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
import json
from .models import Product, Category
from .serializers import (UserSerializer,
                          ProductSerializer,
                          CategorySerializer,
                          ProductSerializer_NotAll,
                          CombinedSerializer)
from apps.user.models import User

import django_filters









class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]



class CategoryListAPIView(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        objects = Category.objects.all()
        serializer = CategorySerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AllUserListAPIView(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    def list(self, request):
         objects = User.objects.all()
         serializer = UserSerializer(objects, many=True)

         return Response(serializer.data, status=status.HTTP_200_OK)

class CategoryCreateAPIView(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    def create(self, request):
        data = request.data.get('data', [])
        for category_data in data:
            serializer = CategorySerializer(data=category_data)
            if serializer.is_valid():
                name = category_data['name']
                Category.objects.get_or_create(name=name)

        return Response({'response': 'created'}, status=status.HTTP_201_CREATED)

class ProductListAPIView(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        products = Product.objects.all()

        serialized_data = []
        for product in products:
            category = Category.objects.filter(id=product.category_id).first()
            user = User.objects.filter(id=product.seller_id).first()

            serializer = ProductSerializer(product)
            serialized_product = serializer.data

            if category:
                serialized_product['category'] = CategorySerializer(category).data
            if user:
                serialized_product['user'] = UserSerializer(user).data

            serialized_data.append(serialized_product)

        return Response(serialized_data, status=status.HTTP_200_OK)

class ProductListDetailAPIView(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    def look(self, request, pk):
        products = Product.objects.filter(pk=pk)

        serialized_data = {}
        for product in products:
            category = Category.objects.filter(id=product.category_id).first()
            user = User.objects.filter(id=product.seller_id).first()


            serializer = ProductSerializer(product)
            serialized_product = serializer.data


            if category:
                serialized_product['category'] = CategorySerializer(category).data
            if user:
                serialized_product['user'] = UserSerializer(user).data


            serialized_data[product.id] = serialized_product

        return Response(serialized_data, status=status.HTTP_200_OK)

class ProductEditAPI(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    def edit(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(instance=product, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['name',]


class ProductFilterListAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        if request.query_parans.get('search'):
            objects = Product.objects.filter(name__contains=request.query_parans.get('search'))
        else:
            objects = Product.objects.all()
        serializer = ProductSerializer(objects, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
