from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
def user_register(request):
    if(request.method=='POST'):
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password']
        password2=request.POST['password2']
        if(password1==password2):
            if(not User.objects.filter(username=username).exists()):
                if(not User.objects.filter(email=email).exists()):
                    user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                    user.save()
                    return redirect('/')
                else:
                    messages.info(request,'Email already registered')
                    return render(request,'register.html')
            else:
                messages.info(request,'Username already registered')
                return render(request,'register.html')
        else:
            messages.info(request,'Password Mismatch')
            return render(request,'register.html')
    else:
        return render(request,'register.html')


def user_login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if(user):
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return render(request,'login.html')
    else:
        return render(request,'login.html')


def user_logout(request):
    auth.logout(request)
    return redirect('/')
