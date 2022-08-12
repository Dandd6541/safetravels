from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Trip(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    stayLength = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name