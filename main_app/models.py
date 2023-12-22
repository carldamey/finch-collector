from django.db import models
from django.urls import reverse

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Finch(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(
      max_length=1,
      choices=MEALS,
      default=MEALS[0][0]
  )
  def __str__(self):
    return f"{self.name} ({self.id})"
  
  def get_absolute_url(self):
    return reverse("detail", kwargs={"finch_id": self.id})