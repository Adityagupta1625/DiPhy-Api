from multiprocessing.sharedctypes import Array
from django.db import models

class Content(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    links=models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Courses(models.Model):
    id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='images/')
    educator=models.CharField(max_length=255)
    content=models.ForeignKey(Content,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Enrolled(models.Model):
    courseid=models.IntegerField()
    studentname=models.CharField(max_length=255)
    
    
