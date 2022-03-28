from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Project


class editProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('approval',)


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('projectAuthor', 'date', 'projectTitle', 'file')


class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=32, required=True, help_text='First Name')
    last_name = forms.CharField(max_length=32, required=True, help_text='Last Name')
    email = forms.CharField(max_length=64, required=True, help_text='email')
