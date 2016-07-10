from django import forms
from .models import IssueLogs

class ABC(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea)

class IssueForm(forms.ModelForm):
    class Meta:
        model = IssueLogs
        fields = ["client", "issueDescription"]