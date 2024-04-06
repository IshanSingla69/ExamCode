from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Test, Question
from .forms import Test_Form
def index(request):
    return render(request, 'teacher/add_test.html', )

# def add_test(request):
#     if request.method == 'POST':
#         form = Test_Form(request.POST)
#         if form.is_valid():
#             form.save()
#             exam_code = genExamCode()
#             test = Test.objects.latest('id')
#             test.examcode = exam_code
#             test_id = test.id
#             test.save()
#             messages.success(request, 'Test created successfully')
#             return redirect('teacher/add_question', test_id=test_id, ques_id=1)
#         else:
#             print(form.errors)
#     else:
#         form = Test_Form()
#     return render(request, 'teacher/add_test.html', {'form': form, 'success': False})

def add_test(request):
    if request.method == 'POST':
        form = Test_Form(request.POST)
        if form.is_valid():
            test = form.save()
            exam_code = genExamCode()
            test.exam_code = exam_code
            test.save()
            question = Question.objects.create(test=test, question_text="")
            return redirect('add_question', test_id=test.pk, q_id=question.pk)
        else:
            form = Test_Form()
        return render(request, 'teacher/add_test.html', {'form': form})

def add_question(request, test_id, q_id=None):
    test = get_object_or_404(Test, pk=test_id)
    if request.method == 'POST':
        question_text = request.POST.get('question_text')
        if question_text and q_id is not None:
            current_question = get_object_or_404(Question, pk=q_id)
            current_question.question_text = question_text
            current_question.save()
        return redirect('add_question', test_id=test.pk, q_id=q_id)
    else:
        if q_id is None:
            current_question = Question.objects.create(test=test, question_text="")
        else:
            current_question = get_object_or_404(Question, pk=q_id)
        all_questions = Question.objects.filter(test=test)
        return render(request, 'createtest/add_question.html', {'test': test, 'question': current_question, 'all_questions': all_questions})
    
def new_question(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    new_question = Question.objects.create(test=test, question_text="")
    return redirect('add_question', test_id=test.pk, q_id=new_question.pk)

def QuestionCreation(request):
    return render(request, 'teacher/QuestionCreationWindow.html')


def genExamCode():
    import random
    import string
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))