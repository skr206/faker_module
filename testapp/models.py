from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=30)
    qualification=models.CharField(max_length=30)
    rollno=models.IntegerField()
    branch=models.CharField(max_length=30)
