from django.db import models
from .species import Species
from .genus import Genus


class Reptile(models.Model):
    name = models.CharField(max_length=50)
    genus = models.ManyToManyField(Genus)
    species = models.ManyToManyField(Species)
