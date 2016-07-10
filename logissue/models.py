from __future__ import unicode_literals

from django.db import models

# Create your models here.

CLIENT_CHOICES = ((1, "Sage UK"),
                  (2, "Sage Global"),
                  (3, "Nespresso"))

class IssueLogs(models.Model):
    issueId = models.AutoField(primary_key=True)
    client = models.IntegerField(choices=CLIENT_CHOICES, blank=False)
    issueDescription = models.TextField(max_length=200 ,blank=False)

