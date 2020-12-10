from django import forms


class LoginForm(forms.Form):
    """Form for handling user login"""
    username = forms.CharField(max_length=2)
    password = forms.CharField(widget=forms.PasswordInput)


