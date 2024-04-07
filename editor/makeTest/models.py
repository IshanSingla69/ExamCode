# models.py
from django.db import models
from django.utils import timezone

class Test(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    datecreated = models.DateTimeField(default=timezone.now)
    total_marks = models.IntegerField()
    exam_code = models.CharField(max_length=200, default='123AB')
    published_bool = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
class PublishedTest(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    datecreated = models.DateTimeField(default=timezone.now)
    total_marks = models.IntegerField()
    exam_code = models.CharField(max_length=200, default='123AB')
    published_bool = models.BooleanField(default=False)

    def __str__(self):
        return self.exam_code

class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    max_marks = models.IntegerField(default=1)
    question_text = models.CharField(max_length=2000)

    def __str__(self):
        return self.question_text