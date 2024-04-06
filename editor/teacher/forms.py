from django import forms
from .models import Test

class Test_Form(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['date_and_time','subject_Code', 'time_Duration', 'total_Marks']
        widgets = {
            'date_and_time': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Enter Test Date and Time'}),
            'subject_Code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Subject Code'}),
            'time_Duration': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'Enter Time Duration'}),
            'total_Marks': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Total Marks'}),
        }
        labels = {
            'date_and_time': '',
            'subject_Code': '',
            'time_Duration': '',
            'total_Marks': '',
        }