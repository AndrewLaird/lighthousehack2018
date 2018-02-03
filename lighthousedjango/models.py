from django.db import models
#
# class User(models.Model):
#     first  = models.CharField(max_length=75)
#     last = models.CharField(max_length=75)
#     #hashed with sha1 and hash lib
#     hashed_password = models.CharField(max_length=500)
#
# class Calendar(models.Model):
#     name =models.CharField(max_length=500)
#     user = models.ForeignKey('User',on_delete=models.PROTECT)


class Event(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    #calendar = models.ForeignKey('Calendar',on_delete=models.PROTECT)

