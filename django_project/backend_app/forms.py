from django import forms

from app.models import Applications


class ApplicationEditForm(forms.ModelForm):
    class Meta:
        model = Applications
        exclude = ['application_id']
