from django.urls import path
from .auth import APIAuthentication
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    api_root,
    Register,
    )

urlpatterns = format_suffix_patterns([
    path('auth/',APIAuthentication.as_view(),name='api-auth'),
    path('register/',Register.as_view(),name='register'),
    path('',api_root,name='root-api')
])
