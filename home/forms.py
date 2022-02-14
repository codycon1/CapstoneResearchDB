from django import forms
from .models import Project


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
