from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.shortcuts import render, redirect


def register(request):
    if request.method=='POST':
        first_name=request.POST["first_name"]
        last_name = request.POST["last_name"]
        u_name = request.POST["u_name"]

        email = request.POST["email"]
        password1=request.POST["psw"]
        password2=request.POST["psw-repeat"]
        if password1==password2:
            if User.objects.filter(username=u_name).exists():
                messages.info(request,'Username already taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=u_name,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print("user created")
        else:
            print("password missmatch")

        return redirect('/')
    else:
        return render(request,'register.html')


def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid details')
            return redirect('login')
    else:
        return render(request,'login.html')
