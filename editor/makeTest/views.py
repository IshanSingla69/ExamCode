# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TestForm
from .models import Test, Question
import string, random

def generate_unique_exam_code():
    while True:
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))  # Generate a random string of 6 uppercase letters and digits
        if not Test.objects.filter(exam_code=code).exists():  # Check if the code is unique
            return code

def create_test(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            test = form.save(commit=False)
            test.exam_code = generate_unique_exam_code()
            test.save()
            question = Question.objects.create(test=test, question_text="", max_marks=1)
            return redirect('makeTest:add_question', test_id=test.pk, q_id=question.pk)
    else:
        form = TestForm()
    tests = Test.objects.all()
    return render(request, 'createtest/create_test.html', {'form': form, 'tests': tests})

def add_question(request, test_id, q_id=None):
    test = get_object_or_404(Test, pk=test_id)
    if request.method == 'POST':
        question_text = request.POST.get('question_text')
        max_marks = request.POST.get('max_marks')
        if question_text and max_marks and q_id is not None:
            current_question = get_object_or_404(Question, pk=q_id)
            current_question.question_text = question_text
            current_question.max_marks = max_marks
            current_question.save()
        return redirect('makeTest:add_question', test_id=test.pk, q_id=q_id)
    else:
        if q_id is None:
            current_question = Question.objects.create(test=test, question_text="", max_marks=1)
        else:
            current_question = get_object_or_404(Question, pk=q_id)
        all_questions = Question.objects.filter(test=test)
        return render(request, 'createtest/add_question.html', {'test': test, 'question': current_question, 'all_questions': all_questions})

def view_question(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    question = Question.objects.filter(test=test).first()  # Get the first question of the test
    all_questions = Question.objects.filter(test=test)
    return render(request, 'createtest/add_question.html', {'test': test, 'question': question, 'all_questions': all_questions})

def new_question(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    new_question = Question.objects.create(test=test, question_text="", max_marks=1)
    return redirect('makeTest:add_question', test_id=test.pk, q_id=new_question.pk)