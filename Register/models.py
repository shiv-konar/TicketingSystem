from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Register(models.Model):
    firstName = models.CharField(max_length=30, blank=False, null=False)
    lastName  = models.CharField(max_length=30, blank=False, null=False)
    email     = models.EmailField(blank=False, null=False)
    timeStamp = models.DateTimeField(auto_now_add=True, auto_now=False)
