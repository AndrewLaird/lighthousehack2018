from django.db import models

class Settings(models.Model):
     black_list = models.CharField(max_length=1000)

class User(models.Model):
    first  = models.CharField(max_length=75)
    last = models.CharField(max_length=75)
    #hashed with sha1 and hash lib
    hashed_password = models.CharField(max_length=500)
    settings = models.ForeignKey('Settings',on_delete=models.PROTECT)

class Calendar(models.Model):
    name =models.CharField(max_length=500)
    user = models.ForeignKey('User',on_delete=models.PROTECT)


class Event(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    calendar = models.ForeignKey('Calendar',on_delete=models.PROTECT)

