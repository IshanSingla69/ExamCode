from django.db import models
from django.utils import timezone
from datetime import timedelta

def one_hour_from_now():
    return timezone.now() + timedelta(hours=1)

# Create your models here.
class Test(models.Model):
    date_and_time = models.DateTimeField(default = one_hour_from_now, blank=False, null=True)
    subject_Code = models.CharField(max_length=100)
    time_Duration = models.DurationField(default=3)
    total_Marks = models.IntegerField(default=100)
    exam_code = models.CharField(max_length=100, default='123AB', blank=False)
    def __str__(self):
        return self.name
class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    ques_id = models.IntegerField()
    question = models.TextField()
    ques_num = models.IntegerField()
    code = models.TextField(default='' , blank=True)
    desired_output = models.TextField()
    max_score = models.IntegerField()
    scored = models.IntegerField()
    
    def __str__(self):
        return self.question