from __future__ import unicode_literals

from django.db import models


class APIData(models.Model):

    api_id = models.IntegerField(unique=True)
    platform = models.CharField(max_length=250)
    date = models.DateTimeField()
    type = models.CharField(max_length=250)
    message = models.CharField(max_length=250)
    expandedLinks = models.URLField()
    link = models.URLField()
    postUrl = models.URLField()
    subscriberCount = models.IntegerField()
    score = models.DecimalField(decimal_places=12, max_digits=20)

    def __str__(self):
        return "This is the APIData"


class Media(models.Model):
    api_data = models.ForeignKey(APIData)
    type = models.CharField(max_length=250)
    url = models.URLField()
    height = models.IntegerField()
    width = models.IntegerField()
    full = models.URLField()

    def __str__(self):
        return "This is the Media"
