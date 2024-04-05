from django.shortcuts import render
from django.http import HttpResponse
from .models import Test, Question
from .forms import Test_Form
def index(request):
    test = Test.objects.all()
    
    return render(request, 'teacher/dashboard.html', {'tests': test})

def add_test(request):
    if request.method == 'POST':
        form = Test_Form(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            subjectCode = form.cleaned_data['subjectCode']
            timeDuration = form.cleaned_data['timeDuration']
            totalMarks = form.cleaned_data['totalMarks']
            test = Test(name=name, subject=subject, subjectCode=subjectCode, timeDuration=timeDuration, totalMarks=totalMarks)
            test.save()
            print('Test added')
            return render(request, 'teacher/add_test.html', {'form': form, 'success': True})
        else:
            print(form.errors)
    else:
        form = Test_Form()
    return render(request, 'teacher/add_test.html', {'form': form, 'success': False})