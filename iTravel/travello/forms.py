from django.forms import ModelForm
from .models import Destination
from django import forms
class DestinationForm(ModelForm):
    class Meta:
        model=Destination
        fields='__all__'
        widgets= {
            'name'  : forms.TextInput(attrs={'class':'inputfield'}),
            'image' : forms.FileInput(attrs={'class':'inputfield' }),
            'desc'  : forms.Textarea(attrs={'class':'inputfield'}),
            'price' : forms.NumberInput(attrs={'class':'inputfield'}),
        }
