from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def home(request):
    return render(request,'home.html',{'name':'This is Page is for Calculations','end':'Thank for Using'})
def add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    v1=int(request.POST['n1'])
    v2=int(request.POST['n2'])
    product=v1*v2
    sum=val1+val2
    return render(request,'result.html',{'mul':product,'result':sum})

def div(request):
    d1=int(request.POST['v1'])
    d2=int(request.POST['v2'])
    division=d1/d2
    return render(request,'result.html',{'di':division})

def sub(request):
    a1=int(request.GET['s1'])
    a2=int(request.GET['s2'])
    min=a1-a2
    return render(request,'result.html',{'subtract':min})