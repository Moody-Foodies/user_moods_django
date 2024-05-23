from rest_framework import serializers
from .models import Mood
from datetime import date
class MoodSerializer(serializers.ModelSerializer):
  class Meta:
    model = Mood
    fields = ('user_id', 'mood', 'date')

  def validate_user_id(self, value):
    if not value:
      raise serializers.ValidationError('User_id is required')
    return value

  def validate(self, attrs):
    if 'date' not in attrs:
      attrs['date'] = date.today()
    return attrs
  
  def to_representation(self, instance):
    ret = super().to_representation(instance)
    if 'date' in ret:
      if isinstance(ret['date'], str):
        ret["date"] = date.fromisoformat(ret['date'])
      ret['date'] = ret['date'].strftime('%Y-%m-%d')
    return ret

class MoodAggregateSerializer(serializers.Serializer):
  avg_mood = serializers.FloatField()
  user_moods = MoodSerializer(many=True)

  def to_representation(self, instance):
    user_moods = instance['user_moods']
    user_id = user_moods[0]['user_id'] if user_moods else None
    data = {
      "data": {
        "id": str(user_id),
        "type": "moods",
        "attributes": {
          "avg_mood": instance["avg_mood"],
          "user_moods": [
            {"date": mood["date"], "mood": mood["mood"]} for mood in user_moods
          ]
        }
      }
    }
    return data