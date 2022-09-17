from django.db import models
from .writer import Writer
from .specialneedsreptile import SpecialNeedsReptile

class SpecialNeedsGuide(models.Model):
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    specialneedsreptile = models.ForeignKey(SpecialNeedsReptile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255)
    content = models.TextField()    