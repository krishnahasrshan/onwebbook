from django.shortcuts import render,redirect
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def showscience_friction(request):
    return render(request,'science-friction.html')
 
 
def Register(request):
    return render(request,'register.html')
