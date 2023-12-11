from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth
# Create your views here.
def register(req):
    if req.method=='POST':
        username=req.POST['username']
        first_name=req.POST['first_name']
        last_name=req.POST['last_name']
        email=req.POST['email']
        password=req.POST['password']
        c_password=req.POST['c_password']
        
        if password==c_password:
            if User.objects.filter(username=username).exists():
                messages.info(req,"User name already exist")
            elif User.objects.filter(password=password).exists():
                 messages.info(req,"password is already exist")  
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password) 

                return redirect('login')
        else:
            messages.info(req,"password not Match")
            return redirect('register')       
    return render(req,'reg.html')

def login(req):
     if req.method=='POST':
        username=req.POST['username']
        password=req.POST['password']
        user=auth.authenticate(username=username,
        password=password)
        print(user)
        if user is not None:
            auth.login(req,user)
            return redirect('/')
        else:
            messages.info(req,"invalid User")
            return redirect('login')
        
     return render(req,'login.html')
def logout(req):
    auth.logout(req)
    return redirect('/')

