from django.db import models
#
class User(models.Model):
    username = models.CharField(max_length=100)
    #hashed with sha1 and hash lib
    hashed_password = models.CharField(max_length=500)
    blocked_websites = models.CharField(max_length=1000)
    totals = models.CharField(max_length=10000)

#
# class Event(models.Model):
#     start = models.DateTimeField()
#     end = models.DateTimeField()
#     title = models.CharField(max_length=500)
#     description = models.CharField(max_length=1000)

