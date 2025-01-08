# members/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.get_members, name='get_members'),
    path('members/create/', views.create_member, name='create_member'),
]
