from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import ExamCodeInput
from makeTest.models import Test, Question
from authentication.models import CustomUser


def index(request):
    if request.method == 'POST':
        examcode = request.POST.get("code").strip()  # Remove leading and trailing whitespace
        matching_tests = Test.objects.filter(exam_code__iexact=examcode)
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
        return render(request, 'student/start_test.html', {'form': form, "name": user})


def attempt_test(request, test_id, q_id):
    test = get_object_or_404(Test, pk=test_id)
    questions = Question.objects.filter(test=test)
    current_question = get_object_or_404(Question, pk=q_id)
    if request.method == 'POST':
        # Handle the form submission here
        pass

    return render(request, 'student/testappear2.html', {'test': test, 'all_questions': questions, 'current_question':current_question})