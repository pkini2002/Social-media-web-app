from django.shortcuts import render,HttpResponse
from .forms import LoginForm

# Create your views here.
def home(request):
    context={}
    return render(request,"base/home.html",context)
    
def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
    else:
        form=LoginForm()
    context={
        'form':form
    }
    return render(request,'base/login.html',context)

def signup(request):
    context={}
    return render(request,"base/signup.html",context)

def friends(request):
    context={}
    return render(request,"base/friends.html",context)
