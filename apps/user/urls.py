from django.urls import path
from .views import LoginAPIView, RegisterView, UserListAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('list/filter/', UserListAPIView.as_view(), name='list-filter'),
]
