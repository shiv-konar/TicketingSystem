from django import forms

class ContactForm(forms.Form):
    fullName = forms.CharField(max_length=30, required=True)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)