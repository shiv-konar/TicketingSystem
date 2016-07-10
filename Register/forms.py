from django import forms
from .models import Register


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        password = forms.CharField(widget=forms.PasswordInput)
        confirmPassword = forms.CharField(widget=forms.PasswordInput)

        fields = ['firstName', 'lastName', 'email', 'password', 'confirmPassword']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirmPassword')

        if not password1:
            raise forms.ValidationError("Please enter a password.")

        if not password2:
            raise forms.ValidationError("Please enter confirmation password.")

        if password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username, provider = email.split("@")
        domain, extenstion = provider.split(".")

        if not domain == "ogilvy":
            raise forms.ValidationError(
                "You are not authorized to create an account. Please contact the administrator.")
