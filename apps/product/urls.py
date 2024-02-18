from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    ProductListAPIView,
    ProductCreateAPIView,
    CategoryCreateAPIView,
    CategoryListAPIView,
    ProductDetailAPIView,
    ProductUpdateAPIView,
    ProductDeleteAPIView,
    ProductViewSet,
    ProductFilterListAPIView, BasketItemViewSet,
)

router = DefaultRouter()
router.register(r'basket', BasketItemViewSet)

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('category/create/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('', ProductListAPIView.as_view(), name='product-list'),
    path('<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('<int:pk>/', ProductUpdateAPIView.as_view(), name='product-update'),
    path('<int:pk>/delete/', ProductDeleteAPIView.as_view(), name='product-delete'),
    path('filter/', ProductFilterListAPIView.as_view(), name='product-filter'),
    path('cart/', BasketItemViewSet.as_view(), name='product-BasketItemViewSet'),
    path('', include(router.urls)),


]
# router = DefaultRouter()
# router.register(r'products', ProductViewSet)
# urlpatterns = router.urls