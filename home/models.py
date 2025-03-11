# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Airgate(models.Model):

    #__Airgate_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    port = models.IntegerField(null=True, blank=True)

    #__Airgate_FIELDS__END

    class Meta:
        verbose_name        = _("Airgate")
        verbose_name_plural = _("Airgate")


class Sensor(models.Model):

    #__Sensor_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    connection = models.IntegerField(null=True, blank=True)

    #__Sensor_FIELDS__END

    class Meta:
        verbose_name        = _("Sensor")
        verbose_name_plural = _("Sensor")


class Employee(models.Model):

    #__Employee_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    chapa = models.IntegerField(null=True, blank=True)

    #__Employee_FIELDS__END

    class Meta:
        verbose_name        = _("Employee")
        verbose_name_plural = _("Employee")



#__MODELS__END
