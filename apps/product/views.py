from django.contrib.sites import requests
from rest_framework import permissions, status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


class ProductListAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Product.objects.all()


class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]



# class ProductListAPIView(APIView):
#     permission_classes = [permissions.AllowAny]
#
#     def get(self, request):
#         objects = Product.objects.all()
#         serializer = ProductSerializer(objects, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


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


class CategoryListAPIView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
    queryset = Category.objects.all()