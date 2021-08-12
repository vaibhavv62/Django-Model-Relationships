from django.db import models
from CollegeApp.models import Dept

# Create your models here.
class Prof(models.Model):
    dept = models.ManyToManyField(Dept)
    name = models.CharField(max_length=32)
    salary = models.FloatField()

    def __str__(self) -> str:
        return f"{self.name},{self.salary}"