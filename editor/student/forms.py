from django import forms

class ExamCodeInput(forms.Form):
    code = forms.CharField(max_length=100)