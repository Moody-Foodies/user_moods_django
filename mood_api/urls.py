from django.urls import path
from .views import (
  MoodListApiView
)

urlpatterns = [
  path('api/', MoodListApiView.as_view())
]