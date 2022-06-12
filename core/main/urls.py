from django.urls import path
from .views import TouristPageListView

urlpatterns = [
    path('', TouristPageListView.as_view(), name='homeBack'),
]