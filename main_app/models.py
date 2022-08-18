from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse

RELATION = (
    ('Family', 'Family'),
    ('Friend', 'Friend'),
    ('Spouse', 'Spouse'),
    ('Significant Other', 'Significant Other'),
    ('Other', 'Other'),
)
# Create your models here.

class People(models.Model):
  name = models.CharField(max_length=50)
  relation = models.CharField(
    max_length=25,
    choices=RELATION,
    default=RELATION[0][1] 
  )
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
    
  def get_absolute_url(self):
    return reverse('peoples_detail', kwargs={'pk': self.id})

class Trip(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    cityFrom = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    stayLength = models.IntegerField()
    date = models.DateField()
    description = models.CharField(max_length=500)
    peoples = models.ManyToManyField(People)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'trip_id': self.id})