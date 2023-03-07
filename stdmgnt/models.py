from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    userid = models.AutoField(primary_key=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now_add=True)
    user_type_options = ((1,"admin"),(2,"student"),(3,"staff"))
    user_type = models.CharField(default=1, choices=user_type_options,max_length=10)

class department(models.Model):
    name =  models.CharField(max_length=10)
    id = models.AutoField(primary_key=True)
    createdDate=models.DateField(auto_now_add=False)
    updatedDate = models.DateTimeField(auto_now_add=True)

class Staff(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    deptid = models.ForeignKey(department.id)
    staffid = models.IntegerField(primary_key=True)

class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    deptid = models.ForeignKey(department.id)
    admnno = models.IntegerField(primary_key=True)
    semester = models.IntegerChoices(choices=range(1,9))

class Subjects(models.Model):
    name = models.CharField(max_length=20)
    id = models.AutoField(primary_key=True)
    departmentid = models.ForeignKey(department.id)
    staff = models.ManyToManyField(Staff)

