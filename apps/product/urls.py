from django.urls import path
from .views import ProductListAPIView, ProductCreateAPIView, CategoryCreateAPIView, CategoryListAPIView

urlpatterns = [
    path('', ProductListAPIView.as_view(), name='product-list'),
    path('create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('category/create/', CategoryCreateAPIView.as_view(), name='product-create'),
    path('category/', CategoryListAPIView.as_view(), name='categorylistAPIView')
]