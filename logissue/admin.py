from django.contrib import admin
from .models import Client, Severity, IssueLog
# Register your models here.

admin.site.register(Client)
admin.site.register(Severity)
admin.site.register(IssueLog)
