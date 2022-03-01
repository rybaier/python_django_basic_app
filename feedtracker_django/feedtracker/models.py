from django.db import models
from django.contrib.auth.models import User



# MEALS = (
#     ('am', 'Breakfast'),
#     ('pm1', 'Lunch'),
#     ('pm2', 'Dinner'),
# )
# Create your models here.

 # unsure if i need to add below to horse class  
#  feed = models.ForeignKey(Feeding, on_delete=models.CASCADE, related_name='feeding')
class Horse(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=100, default='breed unknown')
    markings = models.CharField(max_length=300, default='no visible markings')
    weight = models.CharField(max_length=20)
    height = models.CharField(max_length=30)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')

    def __str__(self):
        return f'{self.name} ({self.id})'


class Feeding(models.Model):
    meal_time = models.CharField(max_length=50)
    hay = models.CharField(max_length=100)
    alfalfa = models.CharField(max_length=100, default = 'no alfalfa')
    grain = models.CharField(max_length=200, default= 'no grain')
    horse = models.ForeignKey(Horse, on_delete=models.CASCADE, related_name='horses')


    def __str__(self):
        return self.horse 

