from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import models
from .models import Mood
from .serializers import MoodSerializer, MoodAggregateSerializer
from datetime import date

class MoodListApiView(APIView):
  def get(self, request, *args, **kwargs):
    user_id = request.query_params.get('user_id')
    if not user_id:
      return Response({"errors":[{"detail": "User_id is required"}]}, status=status.HTTP_400_BAD_REQUEST)
    
    moods = Mood.objects.filter(user_id=user_id)
    if not moods.exists():
      return Response({"data": {"id": user_id, "type": "moods", "attributes": {"avg_mood": 0, "user_moods":[]}}})
    
    mood_serializer = MoodSerializer(moods, many = True)
    
    avg_mood = moods.aggregate(models.Avg('mood'))['mood__avg']

    aggregated_data = {
      'avg_mood': avg_mood,
      'user_moods': mood_serializer.data
    }

    serializer = MoodAggregateSerializer(aggregated_data)
    
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def post(self, request, *args, **kwargs):
    mood = request.data.get('mood')
    user_id = request.data.get('user_id')

    if not user_id or not mood:
      return Response({"errors":{"detail": "User_id and mood are required"}}, status=status.HTTP_400_BAD_REQUEST)
    
    data = {
      'user_id': user_id,
      'mood': mood,
    }
    
    serializer = MoodSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




