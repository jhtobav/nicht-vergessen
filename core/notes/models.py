import datetime

from django.db import models
from django.utils import timezone


class Note(models.Model):
    name = models.CharField(max_length=20)
    text = models.CharField(max_length=200)
    created_date = models.DateTimeField('Date created')

    def __str__(self):
        return self.name

    def was_created_recently(self):
        return self.created_date >= timezone.now() - datetime.timedelta(days=1)