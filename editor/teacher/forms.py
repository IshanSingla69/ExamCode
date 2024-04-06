# forms.py
from django import forms
from .models import Test, Question

class Test_Form(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['subject_Code', 'subject', 'total_Marks']
        widgets = {
            'subject_Code': forms.TextInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'total_Marks': forms.NumberInput(attrs={'class': 'form-control'}),
        }
