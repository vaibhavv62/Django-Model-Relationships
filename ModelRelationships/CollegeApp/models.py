from django.db import models

# Create your models here.
class Dept(models.Model):
    name = models.CharField(max_length=32)
    intake = models.IntegerField()

class Prof(models.Model):
    dept = models.ManyToManyField(Dept)
    name = models.CharField(max_length=32)
    salary = models.FloatField()

class Student(models.Model):
    dept = models.OneToOneField(Dept,on_delete=models.CASCADE)
    rn = models.IntegerField(unique=True)
    name = models.CharField(max_length=32)
    marks = models.FloatField()
