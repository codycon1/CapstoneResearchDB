from django import forms
from .models import proposal


class SubmitProposalForm(forms.ModelForm):
    class Meta:
        model = proposal
        fields = [
            'title',
            'description',
        ]

    def __str__(self):
        return self.title

    # Default approval and user to false / current login user
