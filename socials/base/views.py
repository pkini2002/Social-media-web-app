import email
from multiprocessing import context
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.core.mail import EmailMultiAlternatives,send_mail
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings
from django.views.generic import DetailView,CreateView
from django.contrib.auth.views import PasswordChangeView
from .models import *
from django.urls import reverse_lazy,reverse
from django.views import generic
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'base/home.html'
    posts=Post.objects.all()
    ordering = ['-id']

    def get_context_data(self,*args,**kwargs):
        context=super(HomeView,self).get_context_data(*args,**kwargs)
        page_user=get_object_or_404(Profile)
        context["page_user"]=page_user
        return context

def profile(request):
    context={}
    return render(request,"base/profile.html",context)
    
# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method=="POST":
        login_username=request.POST.get('username', None)
        user_password=request.POST["password"]
        user = authenticate(request,username=login_username, password = user_password)
        if user is not None:
            auth_login(request, user)
            messages.add_message(request, messages.INFO, 'You have successfully logged in.')
            return redirect('/')

        else:
            messages.add_message(request, messages.INFO, 'Invalid username or password.')
            return render(request,"base/login.html")

    return render(request,"base/login.html")

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST': 
        email=request.POST['email']
        password=request.POST['password']
        username=request.POST['username']
        email=email.rstrip()

        if email == '' or password == '' or username == '':
            messages.error(request,"Please fill all the fields.")
            return render(request,"base/signup.html")
        
        elif User.objects.filter(username=username).exists(): 
            messages.add_message(request, messages.INFO, 'Username already exists.')
            return render(request,"base/signup.html")
        
        elif User.objects.filter(email=email).exists():
            messages.add_message(request, messages.INFO, 'Email already exists.')
            return render(request,"base/signup.html")

        else :
            user = User.objects.create(email=email, username=username, password=make_password(password))
            user.save() 
            auth_login(request, user)    
            messages.add_message(request, messages.INFO, 'You have successfully signed up.')
            return redirect('/')
    else:
        return render(request,"base/signup.html")
    

def logout(request):
    auth_logout(request)
    return redirect('/')

# def friends(request):
#     context={}
#     return render(request,"base/friends.html",context)

class FriendView(ListView):
    model = Profile
    template_name = 'base/friends.html'
    profiles=Profile.objects.all()
    ordering = ['-id']

    def get_context_data(self,*args,**kwargs):
        context=super(FriendView,self).get_context_data(*args,**kwargs)
        page_user=get_object_or_404(Profile)
        context["page_user"]=page_user
        return context


def error(request):
    context={}
    return render(request,"base/404.html",context)

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    # fields='__all__'
    template_name = 'base/add_post.html'

class CreateProfilePageView(CreateView):
    model = Profile
    form_class=ProfilePageForm
    template_name="base/create_user_profile.html"
    # fields='__all__'

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class EditProfilePageView(generic.UpdateView):
    model = Profile
    form_class=EditProfileNewForm
    template_name='base/edit_profile_page.html'
    success_url=reverse_lazy('home')

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'base/OtherProfile.html'
    
    def get_context_data(self,*args,**kwargs):
        context=super(ShowProfilePageView,self).get_context_data(*args,**kwargs)
        page_user=get_object_or_404(Profile,id=self.kwargs['pk'])
        context["page_user"]=page_user
        return context

class PasswordsChangeView(PasswordChangeView):
       form_class= PasswordChangingForm
       success_url= reverse_lazy('password_success')

def password_success(request):
    return render(request, 'base/password_success.html', {})

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'base/add_comment.html'

    def form_valid(self,form):
        form.instance.post_id=self.kwargs['pk']
        return super().form_valid(form)

# def LikeView(request,pk):
#     post=get_object_or_404(Post,id=request.POST.get('post.id'))
#     post.likes.add(request.user)
#     return HttpResponseRedirect(reverse('home',args=[str(pk)]))

@login_required(login_url='signup')
def like_post(request):
    username=request.user.username
    post_id=request.GET.get('post_id')
    post=Post.objects.get(id=post_id)
    like_filter=LikePost.objects.filter(post_id=post_id,username=username).first()

    if like_filter==None:
        new_like=LikePost.objects.create(post_id=post_id,username=username)
        new_like.save()

        post.no_of_likes=post.no_of_likes+1
        post.save()
        return redirect('/')

    else:
        like_filter.delete()
        post.no_of_likes=post.no_of_likes-1
        post.save()
        return redirect('/')






