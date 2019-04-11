from django.shortcuts import render,redirect
from django.http import  HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from .models import Profile
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.


def main(request):
	return render(request,"main.html")

def detail(request):
	return render(request,"detail.html")



def myprofile(request):
	if not request.user.is_authenticated:
		return redirect("/")
	profiles= Profile.objects.all()
	context= {'profiles': profiles}
	return render(request,"myprofile.html",context)




def home(request):
	if not request.user.is_authenticated:
		return redirect("/")
	profiles= Profile.objects.all()
	context = {'profiles': profiles}
	return render(request, "home.html", context)

def about(request):
	if request.method == "POST":
		Hobby=request.POST.get('Hobby',None)
		file=request.FILES['file']
		Age=request.POST.get('Age',None)
		Nationality=request.POST.get('Nationality',None)
		Locality=request.POST.get('Locality',None)
		Bio=request.POST.get('Bio',None)
		Phno=request.POST.get('Phno',None)
		Email=request.POST.get('Email')
		print(Hobby)

		# if file.name.endswith(".jpg") or file.name.endswith(".png") or file.name.endswith(".jpeg"):
		profile = Profile.objects.create(
				hobby=Hobby,
				photo=file,
				age=Age,
				nationality=Nationality,
				locality=Locality,
				bio=Bio,
				phno=int(Phno),
				user=request.user
			)
		print(profile)
		return redirect("/home/")
	else:
		return render(request,"about.html")


def signin(request):
	if request.method == "POST":
		username=request.POST.get('username',None)
		password=request.POST.get('password',None)
		print(username,password)
		user = authenticate(request,username=username,password=password)
		print(user)
		if user is not None:
			login(request,user)
			return redirect("/home")
	return render(request,"signin.html")



def signup(request):
	if request.method=='POST':
		fullname=request.POST.get('fullname',None)
		email=request.POST.get('email',None)
		username=request.POST.get('username',None)
		password=request.POST.get('password',None)
		print(password)


		user_exists=User.objects.filter(username=username).exists()
		if not user_exists:
			user=User.objects.create_user(
				username=username,
				password=password,
				email=email,
				first_name=fullname.split()[0],
				last_name=" ".join(fullname.split()[1:])
		)

			login(request,user)
			return redirect("/home")
		else:
			return HttpResponse("User already exists.try new user")
	return render(request,"signup.html")


def signout(request):
	logout(request)
	return redirect("/main")


def sendmail(request, profileid):
	profile = Profile.objects.get(pk = profileid)
	email = profile.user.email

	# email = "vivek.chandra.301096@gmail.com"
	
	print("here is the email")
	msg = EmailMessage("subject", "would like to connect with you.", to=[email])
	msg.send()

	return HttpResponse("email-sent")
