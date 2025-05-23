# api/users/urls.py
from django.urls import path
from . import views

# These paths will be prefixed with 'users/' automatically by the ApiConfig
urlpatterns = [
    path('', views.general_welcome, name='welcome-general'),
    path('info/', views.api_info, name='welcome-api-info'),
]