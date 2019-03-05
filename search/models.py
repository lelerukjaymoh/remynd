from django.conf import settings
from django.db import models
from django.utils import timezone

class search(models.Model):
    search_item = models.CharField(max_length=400)
    date_saved = models.DateTimeField(default=timezone.now)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.search_item
