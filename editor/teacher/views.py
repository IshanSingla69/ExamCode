from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from .models import Test, Question
from .forms import Test_Form, QuestionForm
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
            test_id = test.id
            test.save()
            
            messages.success(request, 'Test created successfully')
            return redirect('teacher/add_question', test_id=test_id, ques_id=1)
        else:
            print(form.errors)
    else:
        form = Test_Form()
    return render(request, 'teacher/add_test.html', {'form': form, 'success': False})

def add_question(request, test_id, ques_id):
    test = Test.objects.get(pk=test_id)
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.test = test
            question.save()
            # Redirect to the next question page
            next_ques_id = ques_id + 1
            return redirect('add_question', test_id=test_id, ques_id=next_ques_id)
    else:
        form = QuestionForm()
    return render(request, 'teacher/add_questions.html', {'form': form, 'test_id': test_id, 'ques_id': ques_id})

def genExamCode():
    import random
    import string
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))