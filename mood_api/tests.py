from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
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


class MoodListApiViewTest(APITestCase):
  def setUp(self):
    Mood.objects.create(user_id=1, mood=1)
    Mood.objects.create(user_id=1, mood=1)
    Mood.objects.create(user_id=2, mood=3)

  def test_get_moods_with_valid_user_id(self):
    url = reverse('mood_list')
    user_id = 1
    response = self.client.get(url, {'user_id': user_id})
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 2)

  def test_get_moods_with_missing_user_id(self):
    url = reverse('mood_list')
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

  def test_post_moods_with_valid_data(self):
    url = reverse('mood_list')
    data = { 'user_id': 1, 'mood': 3 }
    response = self.client.post(url, data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

  def test_post_moods_with_missing_data(self):
    url = reverse('mood_list')
    data = { "user_id": 1 }
    response = self.client.post(url, data)
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)