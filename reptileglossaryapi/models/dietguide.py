from django.db import models
from .writer import Writer
from .reptilediet import ReptileDiet

class DietGuide(models.Model):
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    reptilediet = models.ForeignKey(ReptileDiet, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255)
    content = models.TextField()
    publishing_date = models.DateField(auto_now_add=True)
    