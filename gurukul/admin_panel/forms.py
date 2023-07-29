from django import forms
class loginForm(forms.Form):
    password = forms.CharField(max_length=8)
    email = forms.EmailField()