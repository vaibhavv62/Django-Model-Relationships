from django.db import models
from CollegeApp.models import Dept

# Create your models here.
class Student(models.Model):
    dept = models.ForeignKey(Dept,on_delete=models.CASCADE)
    rn = models.IntegerField(unique=True)
    name = models.CharField(max_length=32)
    marks = models.FloatField()

    def __str__(self) -> str:
        return f"{self.rn},{self.name}"