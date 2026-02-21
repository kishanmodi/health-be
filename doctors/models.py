from django.db import models
from django.conf import settings

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    hospital = models.CharField(max_length=200)

    def __str__(self):
        return self.name