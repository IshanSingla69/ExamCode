from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    subjectCode = models.CharField(max_length=100)
    timeDuration = models.DurationField()
    totalMarks = models.IntegerField()
    examcode = models.CharField(max_length=100, default='123AB', blank=False)
        
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