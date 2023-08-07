from django.db import models
from django.conf import settings as Settings

class Result(models.Model):
    status = models.IntegerField()
    name = models.CharField(max_length=200,default=None)
    command = models.CharField(max_length=200, default=None)
    start_time = models.TextField(blank=True, null=True)
    end_time = models.TextField(blank=True, null=True)
    file = models.CharField(max_length=500, null=True, default=None, blank=True)
