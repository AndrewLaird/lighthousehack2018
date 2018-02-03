from django.db import models


class Event(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    title = models.CharField(500)
    description = models.CharField(1000)

    
