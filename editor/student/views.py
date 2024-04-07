from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from .forms import ExamCodeInput
from makeTest.models import Test, Question
from authentication.models import CustomUser


def index(request):
    if request.method == 'POST':
        examcode = request.POST.get("code").strip()  # Remove leading and trailing whitespace
        matching_tests = Test.objects.filter(exam_code__iexact=examcode)
        print(matching_tests)
        all_test_codes = Test.objects.values_list('exam_code', flat=True)
        print(all_test_codes)
        if matching_tests.exists():
            # The exam code exists
            questions = Question.objects.filter(test=matching_tests.first())
            return redirect('student:attempt_test', test_id=matching_tests.first().pk, q_id=questions.first().pk)
        else:
            # The exam code does not exist
            form = ExamCodeInput()
            user = request.session.get('name','guest')
            return render(request, 'student/start_test.html', {'form': form, "name": user, "error": "Invalid exam code."})
    else:
        form = ExamCodeInput()
        user = request.session.get('name','guest')
        if request.GET.get('submitted') == 'True':
            return render(request, 'student/start_test.html', {'form': form, "name": user,'submitted': True})

        return render(request, 'student/start_test.html', {'form': form, "name": user})


def attempt_test(request, test_id, q_id):
    test = get_object_or_404(Test, pk=test_id)
    questions = Question.objects.filter(test=test)
    current_question = get_object_or_404(Question, pk=q_id)
    if request.method == 'POST':
        # Handle the form submission here
        pass

    return render(request, 'student/testappear2.html', {'test': test, 'all_questions': questions, 'current_question':current_question})

def save_answer(request, test_id, q_id):
    test = get_object_or_404(Test, pk=test_id)
    questions = Question.objects.filter(test=test)
    current_question = get_object_or_404(Question, pk=q_id)
    if request.method == 'POST':
        answer_text = request.POST.get('answer')
        current_question.answer_text = answer_text
        current_question.save()

    return render(request, 'student/testappear2.html', {'test': test, 'all_questions': questions, 'current_question':current_question})

def submit_test(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    questions = Question.objects.filter(test=test)
    if request.method == 'POST':
        context = {
            'test': test,
            'all_questions': questions,
            'submitted': True
        }
        
    return redirect(reverse('student:student_dashboard') + '?submitted=True')