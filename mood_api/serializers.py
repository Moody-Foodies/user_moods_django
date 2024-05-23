from rest_framework import serializers
from .models import Mood
from datetime import date
class MoodSerializer(serializers.ModelSerializer):
  class Meta:
    model = Mood
    fields = ('user', 'mood', 'date')

  def validate(self, attrs):
    if 'date' not in attrs:
      attrs['date'] = date.today()
    return attrs
  
  def to_representation(self, instance):
    ret = super().to_representation(instance)
    ret['date'] = instance.date.strftime('%Y-%m-%d')
    return ret