from django.urls import path

from users.apps import UsersConfig
from users.views import PaymentListAPIView, UserCreateAPIView, UserListAPIView, UserRetrieveAPIView, UserUpdateAPIView, \
    UserDestroyAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = UsersConfig.name

urlpatterns = [
    path('payments/', PaymentListAPIView.as_view(), name='payment_list'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', UserListAPIView.as_view(), name='user_list'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='user_retrieve'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user_delete'),
]
