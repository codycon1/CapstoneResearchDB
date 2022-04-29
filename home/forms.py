from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import ClearableFileInput

from .models import *


class editProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('approval',)


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('projectTitle', 'projectDescription', 'proposalFile')


class UploadProjectFile(forms.ModelForm):
    class Meta:
        model = ProjectFile
        fields = ('file', )


class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=32, required=True, help_text='First Name')
    last_name = forms.CharField(max_length=32, required=True, help_text='Last Name')
    email = forms.CharField(max_length=64, required=True, help_text='email')
