import email
from multiprocessing import context
from django.shortcuts import render,HttpResponse,redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.core.mail import EmailMultiAlternatives,send_mail
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your views here.
def home(request):
    context={}
    return render(request,"base/home.html",context)
    
# Create your views here.
def login(request):
    form=LoginForm()
    context={'form':form}
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST': 
        email_login=request.POST['email']
        login_password=request.POST['password']
        user = authenticate(request, email = email_login, password = login_password)
        if user is not None:
            auth_login(request, user)
            messages.add_message(request, messages.INFO, 'You have successfully logged in.')
            return redirect('/')
        else:
            messages.add_message(request, messages.INFO, 'Invalid email or password.')
            return render(request,"base/login.html",context)
    return render(request,"base/login.html",context)


def signup(request):
    context={}
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST': 
        User = get_user_model()
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm=request.POST['confirmpassword']
        email=email.rstrip()

        if email == '' or password == '' or username == '' or confirm== '':
            messages.error(request,"Please fill all the fields.")
            return render(request,"base/signup.html",context)
        
        elif password != confirm:
            messages.error(request,"Passwords didn't match!")
            return render(request,"base/signup.html",context)

        elif User.objects.filter(email=email).exists():
            messages.add_message(request, messages.INFO, 'Email already exists.')
            return render(request,"base/signup.html",context)

        elif User.objects.filter(username=username).exists():
            messages.add_message(request, messages.INFO, 'Username already exists!')
            return render(request,"base/signup.html",context)

        else :
            user = User.objects.create(email=email,username=username,password=make_password(password))
            user.save() 
            auth_login(request, user)    
            messages.add_message(request, messages.INFO, 'You have successfully signed up.')
            return redirect('/')
    else:
        return render(request,"base/signup.html",context)

def logout(request):
    auth_logout(request)
    return redirect('/')

def friends(request):
    context={}
    return render(request,"base/friends.html",context)

def error(request):
    context={}
    return render(request,"base/404.html",context)
