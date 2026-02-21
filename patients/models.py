from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class Patient(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(120)],
        help_text="Patient age (between 1 and 120)"
    )
    gender = models.CharField(max_length=10)
    diagnosis = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name