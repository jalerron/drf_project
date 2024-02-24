from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from users.apps import UsersConfig
from users.views import PaymentsListAPIView, UserCreateAPIView, UserListAPIView, UserDetailAPIView, UserUpdateAPIView, \
    UserDeleteAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('create/', UserCreateAPIView.as_view(), name='user-create'),
    path('list/', UserListAPIView.as_view(), name='user-list'),
    path('user/<int:pk>/', UserDetailAPIView.as_view(), name='user-retrieve'),
    path('update/<int:pk>', UserUpdateAPIView.as_view(), name='user-update'),
    path('delete/<int:pk>/', UserDeleteAPIView.as_view(), name='user-delete'),


    path('token/', TokenObtainPairView.as_view(), name='token-obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),

    path('payments/', PaymentsListAPIView.as_view(), name='payments-list'),

]
