from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Project


class UploadFileForm(forms.Form):
    projectAuthor = forms.CharField(max_length=1000)
    date = forms.DateField()
    projectTitle = forms.CharField(max_length=100)
    file = forms.FileField()

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=32, required=True, help_text='First Name')
    last_name = forms.CharField(max_length=32, required=True, help_text='Last Name')
    email = forms.CharField(max_length=64, required=True, help_text='email')
