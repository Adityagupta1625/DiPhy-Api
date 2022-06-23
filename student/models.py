from operator import mod
from django.db import models


class Student(models.Model):
    username=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    password=models.CharField(max_length=255)
    

    def __str__(self) -> str:
        return self.username
        