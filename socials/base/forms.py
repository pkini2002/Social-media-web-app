from .models import Profile
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
