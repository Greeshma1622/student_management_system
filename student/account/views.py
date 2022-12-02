from django.shortcuts import render
from .models import Contact,Departments
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'base.html')

def departments(request):
    dict_dept={
        'dept': Departments.objects.all()
    }
    return render(request,'departments.html', dict_dept)
    

def gallery(request):
    return render(request,'gallery.html')

def contact(request):
    if request.method=="POST":
        if request.post['name'] is not None:
            enq=Contact.objects.create(name=request.POST['name'],email=request.POST['email'],phno=request.POST['new_phno'])
            enq.save()
            dicts={'out':1,'name':request.POST['name']}
            return render(request,'contact.html',dicts)
        return render(request,'contact.html')

