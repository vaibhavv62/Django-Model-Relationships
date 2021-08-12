from django.db import models

# Create your models here.
class Dept(models.Model):
    name = models.CharField(max_length=32)
    intake = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.name}"

