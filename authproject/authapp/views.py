from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def home(request):
    return render(request,"index.html")

def login(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        
        user=authenticate(request,username=username,password=password)
        if user:
            login(user)
            return redirect("authapp:home")
        messages.error(request,"Invalid username or password")   
        return redirect("authapp:login")
    
    return render(request,"login.html")

def register(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        confirm_password=request.POST.get("password2")

        if password!= confirm_password:
            messages.info(request,"your two password do not match!!")
            return redirect("authapp:register")
        
        if User.objects.filter(username=username).exists():
            messages.info(request,"This username is already taken")
            return redirect("authapp:register")
        
        user=User(username=username,password=password)
        user.save()

        messages.info(request,"Accoun")
    return render(request,"register.html")

    
def logout_view(request):
    logout(request)
    return redirect("index.html")

 
