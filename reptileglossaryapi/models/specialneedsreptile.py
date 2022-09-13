from django.db import models
from .species import Species
from .morph import Morph

class SpecialNeedsReptile(models.Model):
    name = models.CharField(max_length=50)
    species = models.ManyToManyField(Species)
    morph = models.ManyToManyField(Morph)
