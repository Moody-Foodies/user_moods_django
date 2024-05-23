from django.test import TestCase
from .models import Mood
from datetime import date

class MoodModelTest(TestCase):
  def test_mood_model_exists(self):
    moods = Mood.objects.count()

    self.assertEqual(moods, 0)

  def test_model_has_string_representation(self):
    mood = Mood.objects.create(user_id=1, mood=1)
    expected_string = '%s, %s, %s' % (1, 1, date.today())
    self.assertEqual(str(mood), expected_string)