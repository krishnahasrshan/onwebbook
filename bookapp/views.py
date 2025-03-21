from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import UserProfile
from django.contrib.auth import authenticate

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def showscience_friction(request):
    return render(request,'science-friction.html')
 
 
def Register(request):
    return render(request,'register.html')

def Registerview(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = UserProfile(email=email,
                         password=password)
        user.save()
        
        return render(request,'index.html')
    
from django.contrib import messages
def loginview(request):
    if request.mothod == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(email=email,password=password)
        if user is not None:
            login(request, user)
            messages.success("success")
            return redirect('home')
        else :
            messages.error('invalid')

def logout(request):
     
    logout(request)