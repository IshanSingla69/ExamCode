from django.db import models
from django.utils import timezone
from datetime import timedelta

class Test(models.Model):
    # date_and_time = models.DateTimeField(default = one_hour_from_now, blank=False, null=True)
    subject = models.CharField(max_length=100)
    subject_Code = models.CharField(max_length=100)
    # time_Duration = models.IntegerField(default=2)
    total_Marks = models.IntegerField(default=100)
    exam_code = models.CharField(max_length=100, default='123AB', blank=False)
    def __str__(self):
        return self.name
class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question_text = models.TextField()
    desired_output = models.TextField()
    max_score = models.IntegerField()
    
    def __str__(self):
        return self.question