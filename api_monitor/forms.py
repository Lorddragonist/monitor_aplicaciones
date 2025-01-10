from django import forms
from .models import ApiEndpoint

class ApiEndpointForm(forms.ModelForm):
    class Meta:
        model = ApiEndpoint
        fields = ['name', 'url']
