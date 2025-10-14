from django.urls import path
from . import views

urlpatterns = [
    path('api/register/', views.register_user, name='register_api'),
    path('api/users/', views.list_users, name='list_users'),
]
