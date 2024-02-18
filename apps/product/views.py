from rest_framework import permissions, status, viewsets
from rest_framework import generics
from django.core.cache import cache
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product, Category, BasketItem
from .serializers import ProductSerializer, CategorySerializer, ProductCreateSerializer, BasketItemSerializer, \
    BasketItemSerializer


class ProductListAPIView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = (SearchFilter, OrderingFilter,)
    search_fields = ['name']

class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductCreateSerializer
    permission_classes = [permissions.AllowAny]


class ProductDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Product.objects.all()


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


class ProductUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class ProductFilterListAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        if request.query_params.get('search'):
            objects = Product.objects.filter(name__contains=request.query_params.get('search'))
        else:
            objects = Product.objects.all()
        serializer = ProductSerializer(objects, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, OrderingFilter,)
    search_fields = ['name']



class BasketItemViewSet(viewsets.ModelViewSet):
    queryset = BasketItem.objects.all()
    serializer_class = BasketItemSerializer
