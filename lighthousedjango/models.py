from django.db import models


class Event(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    
