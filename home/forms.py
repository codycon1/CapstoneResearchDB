from django import forms
from .models import Project


class UploadFileForm(forms.Form):
    projectAuthor = forms.CharField(max_length=1000)
    date = forms.DateField()
    projectTitle = forms.CharField(max_length=100)
    file = forms.FileField()

