from django.urls import path
from .views import MagazineListView

urlpatterns = [
    path('magazines/', MagazineListView.as_view(), name='magazine-list'),
]
