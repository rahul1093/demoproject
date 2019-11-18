from django.db import models

# Create your models here.

class Student(models.Model):
    first_name=models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    contact=models.IntegerField(unique=True)
    email=models.EmailField(max_length=50,unique=True)
    age=models.IntegerField()
