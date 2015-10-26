# -*- coding: utf-8 -*-
from django.db import models


class AbstractModel(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return self.name


class City(AbstractModel):
    pass


class Street(AbstractModel):
    pass


class BR(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    skype = models.CharField(max_length=255, blank=True)
    web = models.CharField(max_length=255, blank=True)
    city = models.ForeignKey(City)
    street = models.ForeignKey(Street)
    home = models.PositiveSmallIntegerField()
    index = models.CharField(max_length=8, blank=True)
    flat = models.PositiveSmallIntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.name
