from django.db import models


class Genus(models.Model):

    genus = models.CharField(max_length=50)
