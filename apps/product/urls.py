from django.urls import path

from .views import (CategoryListAPIView,
                    ProductCreateAPIView,
                    CategoryCreateAPIView,
                    AllUserListAPIView,
                    ProductListAPIView,
                    ProductListDetailAPIView,
                    ProductEditAPI,
                    ProductViewSet)



urlpatterns = [
    path('category/create/', CategoryCreateAPIView.as_view({'post': 'create'}), name='category-create'),
    path('category/list/', CategoryListAPIView.as_view({'get': 'list'}), name='category-list'),
    path('all/list/', AllUserListAPIView.as_view({'get': 'list'}), name='all-user-list'),
    path('create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('list/', ProductViewSet.as_view({'get': 'list'}), name='product-list'),
    path('detail/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve'}), name='product-detail'),
    path('edit/<int:pk>', ProductEditAPI.as_view({'patch': 'edit'}), name='product-edit'),
    path('products/', ProductViewSet.as_view({'get': 'list'}), name='product-list'),
]
