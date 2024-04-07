# views.py
from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from .forms import TestForm
from .models import Test, Question,PublishedTest
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
        return render(request, 'createtest/add_question.html', {'test': test, 'question': current_question, 'all_questions': all_questions, 'current_question': current_question})

def view_question(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    question = Question.objects.filter(test=test).first()  # Get the first question of the test
    all_questions = Question.objects.filter(test=test)
    return render(request, 'createtest/add_question.html', {'test': test, 'question': question, 'all_questions': all_questions})

def new_question(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    new_question = Question.objects.create(test=test, question_text="", max_marks=1)
    return redirect('makeTest:add_question', test_id=test.pk, q_id=new_question.pk)

def delete_test(request, test_id):
    if request.method == 'POST':
        test = get_object_or_404(Test, pk=test_id)
        test.question_set.all().delete()  # Delete all questions related to the test
        print(test.question_set.all())
        test.delete()
    return redirect('makeTest:create_test')

from django.shortcuts import redirect, get_object_or_404
from .models import Test, PublishedTest

def publish(request, test_id):
    if request.method == 'POST':
        test_to_copy = get_object_or_404(Test, pk=test_id)
        published_test = PublishedTest()
        name=test_to_copy.name,
        subject=test_to_copy.subject,
        datecreated=test_to_copy.datecreated,
        total_marks=test_to_copy.total_marks,
        exam_code=test_to_copy.exam_code,
        published_bool=True  
        published_test.save()
        test_to_copy.published_bool = True
        test_to_copy.save()
        
        # Redirect to the specified URL
        return redirect('makeTest:create_test')
    else:
        # Handle the case where the request method is not POST
        return HttpResponse("Only POST requests are allowed for this view")


def delete_question(request, test_id, q_id):
    if request.method == 'POST':
        question = get_object_or_404(Question, pk=q_id)
        test = get_object_or_404(Test, pk=test_id)
        question.delete()
        # Get the previous question
        previous_question = Question.objects.filter(test_id=test_id, id__lt=q_id).order_by('-id').first()
        if previous_question is not None:
            return redirect('makeTest:add_question', test_id=test_id, q_id=previous_question.id)
        else:
            # If there is no previous question, get the next question
            next_question = Question.objects.filter(test_id=test_id, id__gt=q_id).order_by('id').first()
            if next_question is not None:
                return redirect('makeTest:add_question', test_id=test_id, q_id=next_question.id)
            else:
                # If there is no next question, redirect to the test
                test.delete()
                return redirect('makeTest:create_test')