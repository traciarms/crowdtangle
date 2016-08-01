from __future__ import unicode_literals

from django.db import models


class ExpectedStatistics(models.Model):
    likeCount = models.IntegerField()
    shareCount = models.IntegerField()
    commentCount = models.IntegerField()

    def __str__(self):
        return "This is the Expected Statistics"


class ActualStatistics(models.Model):
    likeCount = models.IntegerField()
    shareCount = models.IntegerField()
    commentCount = models.IntegerField()

    def __str__(self):
        return "This is the Actual Statistics"


class Account(models.Model):
    api_id = models.IntegerField()
    name = models.CharField(max_length=250)
    handle = models.CharField(max_length=250)
    profileImage = models.URLField(null=True)
    subscriberCount = models.IntegerField()
    url = models.URLField(null=True)
    platform = models.CharField(max_length=250)
    verified = models.BooleanField()

    def __str__(self):
        return "This is the Account"


class APIData(models.Model):
    api_id = models.IntegerField(unique=True)
    platform = models.CharField(max_length=250)
    date = models.DateTimeField()
    type = models.CharField(max_length=250)
    message = models.CharField(max_length=250)
    expandedLinks = models.URLField(null=True)
    link = models.URLField(null=True)
    postUrl = models.URLField(null=True)
    subscriberCount = models.IntegerField()
    score = models.DecimalField(decimal_places=12, max_digits=20)
    exp_statistics = models.ForeignKey(ExpectedStatistics, null=True)
    act_statistics = models.ForeignKey(ActualStatistics, null=True)
    account = models.ForeignKey(Account, null=True)

    def __str__(self):
        return "This is the APIData"


class Media(models.Model):
    api_data = models.ForeignKey(APIData, on_delete=models.CASCADE)
    type = models.CharField(max_length=250)
    url = models.URLField(null=True)
    height = models.IntegerField()
    width = models.IntegerField()
    full = models.URLField(null=True)

    def __str__(self):
        return "This is the Media"

