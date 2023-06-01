from django.db import models
from django.urls import reverse
from datetime import date

TASKS = (
  ('C', 'Spook the Children'),
  ('A', 'Avoid Capture'),
  ('S', 'Setup the Sequel')
)

class Monster(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()

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