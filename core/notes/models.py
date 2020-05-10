import datetime

from django.db import models
from django.utils import timezone


class Note(models.Model):
    note_title = models.CharField(max_length=20)
    note_content = models.CharField(max_length=200)
    note_last_updated_time = models.DateTimeField('Last time updated')

    def __str__(self):
        return self.name

    def was_modified_recently(self):
        return self.note_last_updated_time >= timezone.now() - datetime.timedelta(days=1)