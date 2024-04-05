from django import forms
from .models import Test

class Test_Form(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['name', 'subject', 'subjectCode', 'timeDuration', 'totalMarks']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Test Name'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Subject'}),
            'subjectCode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Subject Code'}),
            'timeDuration': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'Enter Time Duration'}),
            'totalMarks': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Total Marks'}),
        }
        labels = {
            'name': '',
            'subject': '',
            'subjectCode': '',
            'timeDuration': '',
            'totalMarks': '',
        }