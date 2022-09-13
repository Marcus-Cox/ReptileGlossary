from django.db import models


class Morph(models.Model):

    morph = models.CharField(max_length=50)
