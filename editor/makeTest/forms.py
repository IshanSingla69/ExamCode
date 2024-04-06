# forms.py
from django import forms
from .models import Test

class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['name', 'subject', 'total_marks']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'total_marks': forms.NumberInput(attrs={'class': 'form-control'}),
        }