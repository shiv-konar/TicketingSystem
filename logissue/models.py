from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Client(models.Model):
    client_name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.client_name

class Severity(models.Model):
    severity_index = models.CharField(max_length=10)

    def __unicode__(self):
        return self.severity_index


class IssueLog(models.Model):
    client_name = models.ForeignKey(Client)
    issue_description = models.TextField(max_length=200)
    issued_by = models.ForeignKey(User, related_name="%(class)s_requests_created")
    issued_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    severity_index = models.ForeignKey(Severity)
    assigned_to = models.ForeignKey(User, default=None, blank=True, null=True)
    is_escalated = models.BooleanField(default=False)
    is_open = models.BooleanField(default=True)

    def __unicode__(self):
        return self.issue_description


class AddMessage(models.Model):
    issue_description = models.ForeignKey(IssueLog)
    additional_information = models.TextField(max_length=200)
    added_on = models.DateTimeField(auto_now_add=True, auto_now=False)


