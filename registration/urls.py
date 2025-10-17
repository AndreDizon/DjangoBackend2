# registration/urls.py

from django.urls import path
from . import views 
# OR from .views import register_user # Depending on how you import

urlpatterns = [
    # This is the line that must exist and match 'api/register/'
    path('api/register/', views.register_user, name='register_api'),
    # ... any other URLs for the registration app ...
    path('api/users/', views.list_user, name='list_users'),  # New endpoint for listing users
    path('api/users/<int:pk>/', views.user_detail, name='user_detail'),  # New endpoint for user details
]

