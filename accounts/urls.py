from django.urls import path, include
from .views import SignUpAPIView, CheckUserTypeAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('auth/signup/', SignUpAPIView.as_view(), name='signup'),
    path('auth/signin/token/', TokenObtainPairView.as_view(), name='sign_token'),
    path('auth/signin/token/refresh/',
         TokenRefreshView.as_view(), name='sign_token_refresh'),
    path('auth/check_user_type/',
         CheckUserTypeAPIView.as_view(), name='check_user_type'),

]

urlpatterns += [
    path('auth/direct/', include('rest_framework.urls')),
]
