from django import forms
from .models import ServerModel

class ServerModelForms(forms.ModelForm):
    class Meta:
        model = ServerModel
        fields = ['hostname']
