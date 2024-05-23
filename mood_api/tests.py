from django.test import TestCase
from .models import Mood

class MoodModelTest(TestCase):
  def test_mood_model_exists(self):
    moods = Mood.objects.count()

    self.assertEqual(moods, 0)
