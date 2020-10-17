from django import forms
import unicodedata


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label='Password', strip=False, widget=forms.PasswordInput)

    error_messages = {
        'invalid_login':
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ,
        'inactive': "This account is inactive.",
    }
