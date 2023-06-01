from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

TASKS = (
  ('C', 'Spook the Children'),
  ('A', 'Avoid Capture'),
  ('S', 'Setup the Sequel')
)

class Bane(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse("bane-detail", kwargs={"pk": self.id})

class Monster(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  banes = models.ManyToManyField(Bane)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse("monster-detail", kwargs={"monster_id": self.id})

  def finished_for_today(self):
    return self.checklist_set.filter(date=date.today()).count() >= len(TASKS)
  
class Checklist(models.Model):
  date = models.DateField('Date Completed')
  task = models.CharField(
    max_length=1,
    choices=TASKS,
    default=TASKS[0][0])
  
  monster = models.ForeignKey(Monster, on_delete=models.CASCADE)

  def __str__(self): 
    return f"{self.get_task_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']

  