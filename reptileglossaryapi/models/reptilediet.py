from django.db import models
from .diet import Diet
from .reptile import Reptile

class ReptileDiet(models.Model):
    type = models.CharField(max_length=50)
    reptile = models.ManyToManyField(Reptile)
    diet = models.ManyToManyField(Diet)
