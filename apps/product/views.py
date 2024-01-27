from rest_framework import permissions, status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product, Category
from apps.user.models import User
from apps.user.serializers import UserSerializer
from .serializers import ProductSerializer, CategorySerializer


class ProductListAPIView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]


class CategoryListAPIView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryCreateAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        data = request.data.get('data', [])
        for category_data in data:
            serializer = CategorySerializer(data=category_data)
            if serializer.is_valid():
                name = category_data['name']
                Category.objects.get_or_create(name=name)
        return Response({'response': 'created'}, status=status.HTTP_201_CREATED)