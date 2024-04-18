
# todo/models.py
      
from django.db import models
# Create your models here.

# add this
class Todo(models.Model):

  YEAR_IN_SCHOOL_CHOICES = [
      ("FR", "Freshman"),
      ("SO", "Sophomore"),
      ("JR", "Junior"),
      ("SR", "Senior"),
      ("GR", "Graduate"),
  ]

  title = models.CharField(max_length=120)
  description = models.TextField()
  completed = models.BooleanField(default=False)
  status = models.Choice
      
  def __str__(self):
    return self.title