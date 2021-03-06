from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        if request.POST['password1']==request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username1'])
                return render(request,'accounts/signup.html',{'error':'Username has already been taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username1'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('restuarant:Home')
        else:
            return render(request,'accounts/signup.html',{'error':'Password doesn\'t match!'})
    else:
        return render(request,'accounts/signup.html')

def login(request):
    if request.method=='POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('restuarant:Home')
        else:
            return render(request,'accounts/login.html',{'error':'Username or Password is incorrect!'})
    else:
        return render(request,'accounts/login.html')


def logout(request):
    if request.method=='GET':
        auth.logout(request)
        return redirect('restuarant:Home')
