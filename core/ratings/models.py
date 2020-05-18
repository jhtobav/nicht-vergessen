import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Rating(models.Model):
    rating_title = models.CharField(max_length=30)
    rating_type = models.CharField(max_length=10)
    rating_score = models.FloatField()
    rating_review = models.CharField(max_length=200)
    rating_creation_date = models.DateTimeField("Rating creation date")

    def __str__(self):
        return self.rating_title

    def was_rated_recently(self):
        return self.rating_creation_date >= timezone.now() - datetime.timedelta(days=1)
