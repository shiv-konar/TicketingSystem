from django import forms
from .models import IssueLog, AddMessage


class IssueLogForm(forms.ModelForm):
    class Meta:
        model = IssueLog
        fields = ["client_name", "issue_description", "severity_index"]


class AddMessageForm(forms.ModelForm):
    class Meta:
        model = AddMessage
        fields = ["additional_information"]