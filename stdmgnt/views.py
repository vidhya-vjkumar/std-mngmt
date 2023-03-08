from django.shortcuts import render
from stdmgnt.models import Student

# Create your views here.
def home(request):
    return render(request,'details.html')

def details(request):
    if request.method=="POST":
        name=request.POST['name']
        address=request.POST['address']
        admnno=request.POST['admnno']
        semester=request.POST['semester']
        info=Student(name=name,address=address,admnno=admnno,semester=semester)
        info.save()
    return render(request,"details.html")