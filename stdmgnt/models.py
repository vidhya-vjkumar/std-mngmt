from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(models.Model):
    userid = models.AutoField(primary_key=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now_add=True)
    user_type_options = ((1,"HOD"),(2,"Staff"),(3,"Student"))
    user_type = models.IntegerField(default=1, choices=user_type_options)

class Department(models.Model):
    name =  models.CharField(max_length=10)
    id = models.AutoField(primary_key=True)
    createdDate=models.DateField(auto_now_add=False)
    updatedDate = models.DateTimeField(auto_now_add=True)

class Staff(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    dept= models.ForeignKey(Department, on_delete=models.CASCADE)
    staffid = models.IntegerField(primary_key=True)

class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    admnno = models.IntegerField(primary_key=True)
    semester = models.IntegerField()

class Subjects(models.Model):
    name = models.CharField(max_length=20)
    id = models.AutoField(primary_key=True)
    departmentid = models.ForeignKey(Department, on_delete=models.CASCADE)
    staff = models.ManyToManyField(Staff)

