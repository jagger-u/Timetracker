from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class DailyAct(models.Model):
  act_name = models.CharField(max_length=100)
  start_time = models.DateTimeField()
  end_time = models.DateTimeField()
  act_date = models.CharField(max_length=100)
  act_comments = models.TextField(null=True) #maybe this is where have the problem!
  def __str__(self):
    return self.act_name
  def calcDiff(self):
    self.time_diff = self.end_time - self.start_time
    return self.time_diff
  def calcDiff_show(self):
    self.time_diff = self.end_time - self.start_time
    return str(self.time_diff)[:-3]            #just a trick to not show the seconds

class Tag(models.Model):
  name = models.CharField(max_length=50, unique=True)
  def __str__(self):
    return "Tag is: {}".format(self.name)

class ourDays(models.Model):
  day_date = models.CharField(max_length=100, unique=True)
  day_tags = models.ManyToManyField(Tag)
  sum_time = timedelta(0)
  def dayTotal(self):
    all_acts_for_a_day = DailyAct.objects.filter(act_date=self.day_date).all()
    self.sum_time = timedelta(0)
    for idx in range(len(all_acts_for_a_day)):
      self.sum_time = self.sum_time + all_acts_for_a_day[idx].calcDiff()
    return self.sum_time
  def __str__(self):
    return "Day: {}, Total: {}".format(self.day_date, self.sum_time)
