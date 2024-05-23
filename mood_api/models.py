from django.db import models
from django.contrib.auth.models import User

class Mood(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  mood = models.IntegerField(blank = False)
  date = models.DateTimeField(auto_now = True, blank = False)
  created = models.DateTimeField(auto_now = True, blank = True)

  def __str__(self):
    return '%s, %s, %s' % (self.user, self.mood, self.date)
