from .models import Profile,Post,Comment
from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User

class EditProfileNewForm(forms.ModelForm):
     class Meta:
       model=Profile
       fields = ('username','fname','lname','description','profileimg')

       widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'fname':forms.TextInput(attrs={'class':'form-control'}),
            'lname':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
        }

class ProfilePageForm(forms.ModelForm):
    class Meta:
       model=Profile
       fields = ('username','fname','lname','description','profileimg')

       widgets={
          'username':forms.TextInput(attrs={'class':'form-control'}),
          'fname':forms.TextInput(attrs={'class':'form-control'}),
          'lname':forms.TextInput(attrs={'class':'form-control'}),
          'description':forms.Textarea(attrs={'class':'form-control'}), 
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author','caption','location','image')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title tag'}),
            'author':forms.Select(attrs={'class':'form-control'}),
            'caption':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Content'}),
            'location':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Location'}),
        }

class PasswordChangingForm(PasswordChangeForm):
    old_password=forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control', 'type':'password'}))
    new_password1=forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    new_password2=forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))

    class Meta:
        model= User
        fields = ('old_password','new_password1','new_password2')

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','body')

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
       }

class EditForm(forms.ModelForm):
    class Meta:
        model=Post
        fields = ('title','title_tag','author','caption','location','image')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title tag'}),
            'author':forms.Select(attrs={'class':'form-control','placeholder':'username'}),
            'caption':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Content'}),
            'location':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Location'}),
        }
