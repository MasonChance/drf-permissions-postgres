from django.db import models
from django.contrib.auth.models import User 

# !!! created with snippet, add properties and alter __str__ as needed
class Deck(models.Model):
    name = models.CharField(max_length=64)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    mana_type = models.CharField(max_length=64)
    cast_cost = models.CharField(max_length=64)
    size = models.IntegerField()
    
    def __str__(self):
         return self.name



# Create your models here.
