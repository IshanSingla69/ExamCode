from django.shortcuts import render
from django.http import HttpResponse
from .forms import ExamCodeInput
from teacher.models import Test
from authentication.models import CustomUser


def index(request):
    if request.method == 'POST':
        examcode_ = request.POST.get("code")
        matchingtest = Test.objects.filter(subjectCode = examcode_)
        return render(request, 'student/testAppear.html')
    else:
        form = ExamCodeInput()
        user = request.session.get('name','guest')
    return render(request, 'student/start_test.html', {'form': form,"name":user})


def test(request):
    return render(request, 'student/testAppear.html')


