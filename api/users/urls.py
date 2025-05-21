# api/users/urls.py
from django.urls import path
from . import views

# These paths will be prefixed with 'users/' automatically by the ApiConfig
urlpatterns = [
    path('', views.list_users, name='user-list'),
    path('<int:user_id>/', views.user_detail, name='user-detail'),
]