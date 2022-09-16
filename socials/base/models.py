from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    gender_choices=[('1','Male'),('2','Female'),('3','Dont want to specify')]
    id=models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    gender=models.CharField(max_length=1,choices=gender_choices,default='1')
    phone=models.CharField(blank=True, max_length=10,default='')
    DOB=models.DateField(null=True)
    image=models.ImageField(blank=True,upload_to='images/user', height_field=None, width_field=None, max_length=100,null=True)

    def __str__(self):
        return f'{self.user.username} Profile'