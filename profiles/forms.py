from django import forms

from . import models

class ProfileForm(forms.ModelForm):
    class Meta:
        model=models.Profiles
        fields='__all__'

