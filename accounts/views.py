from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def register(req):

    if req.method == 'POST':
        
        uname = req.POST['username']
        password = req.POST['password']

        if User.objects.filter(username=uname).exists():
            messages.info(req,'Username taken')
            return redirect('accounts:register')

        user = User.objects.create_user(username=uname,password=password)
        print(user)

        return redirect('accounts:login')

    return render(req,'register.html')


def login(req):

    if req.method == 'POST':

        uname = req.POST['username']
        password = req.POST['password']

        print(uname,password)

        user = auth.authenticate(username=uname,password=password)

        print(user)

        if user is not None:
            auth.login(req,user)
            return redirect('/')
        

        messages.info(req,'Invalid username or password')
        return redirect('login')
        
       
    return render(req,'login.html')


def logout(req):
    auth.logout(request=req)
    return redirect('/')