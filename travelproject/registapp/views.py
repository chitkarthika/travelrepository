from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def logoutpg(request):
    print("Entered logout def")
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(username=uname,password=pwd)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"INVALID CREDENTIALS")
            return redirect('login')
    return render(request,"login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pwd = request.POST['pwd1']
        cpwd = request.POST['pwd2']
        if pwd == cpwd:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Already Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,first_name=fname,last_name=lname,email=email,password=pwd)
                user.save();

                print("*******New User created*******")
                return redirect('login')
        else:
            messages.info(request,"Password not matching ")
            print("Password not matching")
            return redirect('register')

    return render(request,"register.html")


def test(request):
    print("Entered test def")
    if request.method == 'POST':
        return redirect('register')
    return render(request,"testpage.html")
