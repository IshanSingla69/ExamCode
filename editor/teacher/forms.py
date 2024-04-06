from django import forms
from .models import Test, Question

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
        
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question', 'ques_num', 'code', 'desired_output', 'max_score']
        widgets = {
            'question': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Question'}),
            'ques_num': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Question Number'}),
            'code': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Code'}),
            'desired_output': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Desired Output'}),
            'max_score': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Maximum Score'}),
        }
        labels = {
            'question': '',
            'ques_num': '',
            'code': '',
            'desired_output': '',
            'max_score': '',
        }