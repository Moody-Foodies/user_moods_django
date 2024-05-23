from django.db import models
from datetime import date

class Mood(models.Model):
  user_id = models.IntegerField(default=0, blank=False)
  mood = models.IntegerField(blank = False)
  date = models.DateField(default=date.today, blank = False)
  created = models.DateTimeField(auto_now = True, blank = True)

  def __str__(self):
    return '%s, %s, %s' % (self.user_id, self.mood, self.date)
