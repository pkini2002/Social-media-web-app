from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
from ckeditor.fields import RichTextField
from django.urls import reverse

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    fname = models.TextField(blank=True)
    lname = models.TextField(blank=True)
    username=models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')

    def __str__(self):
        return(str(self.user)) 

    def get_absolute_url(self):
        return reverse('home')

class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user

class Post(models.Model):
    title=models.CharField(max_length=255)
    image=models.ImageField(null=True,blank=True,upload_to="images/")
    title_tag=models.CharField(max_length=255,default="")
    author=models.ForeignKey(Profile,on_delete=models.CASCADE)
    caption=RichTextField(blank=True,null=True)
    post_date=models.DateField(auto_now_add=True)
    location=models.CharField(max_length=255,default="")
    no_of_likes=models.IntegerField(default=0)

    def __str__(self):
        return self.title + " | " + str(self.author)

    def get_absolute_url(self):
        return reverse('home')

    def get_owner_pp(self):
        return self.author.profileimg.url

    def profileid(self):
        return self.author.user.id

class Comment(models.Model):
    post=models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    body=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title,self.name)

    def get_absolute_url(self):
        return reverse('home')

class LikePost(models.Model):
    post_id=models.CharField(max_length=500)
    username=models.CharField(max_length=100)

    def __str__(self):
        return self.username



