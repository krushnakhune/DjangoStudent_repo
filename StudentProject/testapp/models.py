from django.db import models

class StudentData(models.Model):
    student_roll=models.IntegerField(unique=True)
    student_fname=models.CharField(max_length=100)
    student_lname=models.CharField(max_length=100)
    student_class=models.CharField(max_length=20)
    student_section=models.CharField(max_length=20)
    telugu=models.IntegerField()
    hindi=models.IntegerField()
    english=models.IntegerField()
    maths=models.IntegerField()
    science=models.IntegerField()
    social=models.IntegerField()
