from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
	hobby=models.CharField(max_length=100,blank=True)
	photo =models.ImageField(upload_to='pic-folder/',default='pic-folder/default.png')
	age=models.IntegerField(default=25,blank=True)
	nationality=models.CharField(max_length=100,blank=True)
	locality=models.CharField(max_length=100,blank=True)
	bio=models.TextField(max_length=200,blank=True)
	phno=models.IntegerField(default=10,blank=True)
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	email=models.EmailField(default=True,blank=True)


	