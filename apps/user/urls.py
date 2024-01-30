from django.urls import path
from .views import LoginAPIView, SellerRegisterView, UserListAPIView, BuyerRegisterView, BuyerListAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('register/seller/', SellerRegisterView.as_view(), name='register-seller'),
    path('user/', UserListAPIView.as_view(), name='userlistAPIView'),
    path('buyer/', BuyerListAPIView.as_view(), name='buyerlistAPIView'),
    path('register/buer/', BuyerRegisterView.as_view(), name='register-buer'),
]