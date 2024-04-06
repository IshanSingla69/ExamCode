from django.shortcuts import render
from django.http import HttpResponse
from .forms import ExamCodeInput
from teacher.models import Test
from authentication.models import CustomUser


def index(request):
    if request.method == 'POST':
        examcode = request.POST.get("code")

        # Check if the exam code exists
        matching_tests = Test.objects.filter(exam_code=examcode)
        if matching_tests.exists():
            # The exam code exists
            return render(request, 'student/testAppear.html')
        else:
            # The exam code does not exist
            form = ExamCodeInput()
            user = request.session.get('name','guest')
            return render(request, 'student/start_test.html', {'form': form, "name": user, "error": "Invalid exam code."})
    else:
        form = ExamCodeInput()
        user = request.session.get('name','guest')
        return render(request, 'student/start_test.html', {'form': form, "name": user})


def test(request):
    return render(request, 'student/testAppear2.html')


