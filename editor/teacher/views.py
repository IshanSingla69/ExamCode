from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from .models import Test, Question
from .forms import Test_Form
def index(request):
    test = Test.objects.all()
    
    return render(request, 'teacher/dashboard.html', {'tests': test})

def add_test(request):
    if request.method == 'POST':
        form = Test_Form(request.POST)
        if form.is_valid():
            form.save()
            exam_code = genExamCode()
            test = Test.objects.latest('id')
            test.examcode = exam_code
            test.save()
            
            messages.success(request, 'Test created successfully')
            return redirect('teacher:add_question')
        else:
            print(form.errors)
    else:
        form = Test_Form()
    return render(request, 'teacher/add_test.html', {'form': form, 'success': False})

def add_question(request):
    
    return render(request, 'teacher/add_questions.html')

def genExamCode():
    import random
    import string
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))