from django.urls import path
from .views import (ProductListAPIView,
                    ProductCreateAPIView,
                    CategoryCreateAPIView,
                    CategoryListAPIView,
                    ProductDetailAPIView, ProductUpdateAPIView,
                    )

urlpatterns = [
    path('', ProductListAPIView.as_view(), name='product-list'),
    path('create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('category/create/', CategoryCreateAPIView.as_view(), name='product-create'),
    path('category/', CategoryListAPIView.as_view(), name='categorylistAPIView'),
    path('products/<int:id>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('products/<int:id>/update/', ProductUpdateAPIView.as_view(), name='product-update'),
]