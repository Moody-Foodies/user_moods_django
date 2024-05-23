from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Mood
from.serializers import MoodSerializer

class MoodListApiView(APIView):
  def get(self, request, *args, **kwargs):
    moods = Mood.objects.filter(user = request.user_id)
    serializer = MoodSerializer(moods, many = True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def post(self, request, *args, **kwargs):
    data = {
      'mood': request.data.get('mood'),
      'date': request.data.get('date'),
      'user': request.user_id
    }

    serializer = MoodSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




