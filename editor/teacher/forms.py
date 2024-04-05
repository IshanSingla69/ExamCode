from django import forms

class Test_Form(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Test Name'}))
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Subject'}))
    subjectCode = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Subject Code'}))
    timeDuration = forms.DurationField(widget=forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'Enter Time Duration'}))
    totalMarks = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Total Marks'}))
    