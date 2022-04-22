from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *


# class SubmitProposalForm(forms.ModelForm):
#     class Meta:
#         model = Proposal
#         fields = [
#             'title',
#             'description',
#         ]
#
#     def __str__(self):
#         return self.title
#
#     # Default approval and user to false / current login user


class editProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('approval',)


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('projectTitle', 'projectDescription', 'proposalFile')


class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=32, required=True, help_text='First Name')
    last_name = forms.CharField(max_length=32, required=True, help_text='Last Name')
    email = forms.CharField(max_length=64, required=True, help_text='email')
