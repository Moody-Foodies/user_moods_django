from django.urls import path
from .views import (
  MoodListApiView
)

urlpatterns = [
  path('moods/', MoodListApiView.as_view(), name='mood_list')
]