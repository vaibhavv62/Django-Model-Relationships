from django.db import models
from CollegeApp.models import Dept

# Create your models here.
class Prof(models.Model):
    dept = models.ManyToManyField(Dept)
    name = models.CharField(max_length=32)
    salary = models.FloatField()

    def __str__(self) -> str:
        return f"{self.name},{self.salary}"

    ret = ""
    def get_dept_values(self):
        global ret
        print(self.dept.all())
        for dept in self.dept.all():
            print('Hello',dept.name)
            print(f"self.ret-{self.ret}")
            self.ret = self.ret + dept.name + ","
            print(self.ret[::])
        return self.ret