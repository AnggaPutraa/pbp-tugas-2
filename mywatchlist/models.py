from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class WatchItem(models.Model):
    watched = models.BooleanField()
    title = models.CharField(
        max_length = 255
    )
    rating = models.IntegerField(
        validators= [
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    release_date = models.TextField()
    review = models.CharField(
        max_length = 255 
    )
