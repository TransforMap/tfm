from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import JSONField


class Owner(models.Model):
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Map(models.Model):
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class MapObject(models.Model):
    data = JSONField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

