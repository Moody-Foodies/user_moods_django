from django.db import models
from django.contrib.auth.models import User

class Mood(models.Model):
  user_id = models.IntegerField(blank=False)
  mood = models.IntegerField(blank = False)
  date = models.DateTimeField(auto_now = True, blank = False)

  def __str__(self):
    return '%s, %s, %s' % (self.user_id, self.mood, self.date)
