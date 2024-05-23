from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Mood
from.serializers import MoodSerializer

class MoodListApiView(APIView):
  def get(self, request, *args, **kwargs):
    user_id = request.query_params.get('user_id')
    if not user_id:
      return Response({"errors":{"detail": "User_id is required"}}, status=status.HTTP_400_BAD_REQUEST)
    moods = Mood.objects.filter(user_id=user_id)

    serializer = MoodSerializer(moods, many = True)
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




