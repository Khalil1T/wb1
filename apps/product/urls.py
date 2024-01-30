from django.urls import path
from .views import (ProductListAPIView,
                    ProductCreateAPIView,
                    CategoryCreateAPIView,
                    CategoryListAPIView,
                    ProductDetailAPIView,
                    ProductUpdateAPIView,
                    ProductDeleteAPIView,
                    )

urlpatterns = [
    path('', ProductListAPIView.as_view(), name='product-list'),
    path('create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('category/create/', CategoryCreateAPIView.as_view(), name='cateogry-create'),
    path('category/', CategoryListAPIView.as_view(), name='categorylistAPIView'),
    path('product/<int:id>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('product/<int:pk>/update/', ProductUpdateAPIView.as_view(), name='product-update'),
    path('product/<int:pk>/delete/', ProductDeleteAPIView.as_view(), name='product-delete'),
]