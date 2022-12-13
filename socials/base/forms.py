from .models import Profile,Post
from django import forms

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
        fields = ('title','title_tag','author','caption','image')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title tag'}),
            'author':forms.Select(attrs={'class':'form-control','placeholder':'username'}),
            'caption':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Content'}),
        }
