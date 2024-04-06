from django import forms
from .models import Test, Question

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