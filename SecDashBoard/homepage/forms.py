from django import forms
from .models import PromServerModel

class PromServerModelForms(forms.ModelForm):
    class Meta:
        model = PromServerModel
        fields = ['hostname']
