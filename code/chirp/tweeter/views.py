from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from .models import *

from django.utils import timezone

def index(request):
	return render(request, 'tweeter/index.html')

def auth(request):
	username = request.POST['user']
	password = request.POST['pass']
	try:
		user = User.objects.get(handle=username)
	except Exception as e:
		return HttpResponse("This user handle does not belong to anyone!")
	else:
		uid = user.uid
		pwd = UserLoginCredentials.objects.get(uid=uid).pwd
		if(password == pwd):
			#return HttpResponse('Login successful!')
			return HttpResponseRedirect('http://localhost:8000/tweeter/' + username)
		else:
			return HttpResponse('Invalid username and password combination!')

def user_profile(request, handle):
	try:
		user = User.objects.get(handle=handle)
	except Exception as e:
		return HttpResponse("This user handle does not belong to anyone!")
	else:
		tweets = Tweet.objects.all().filter(author=user).order_by('-ts')
		context = {'user': user, 'tweets': tweets}
		return render(request, 'profile-page/index.html', context)

def following(request, handle):
	try:
		this_user = User.objects.get(handle=handle)
	except Exception as e:
		return HttpResponse("This user handle does not belong to anyone!")
	else:
		users = '<br/><br/>'.join([str(user) for user in this_user.following.iterator()])
		return HttpResponse(users)

def followers(request, handle):
	try:
		this_user = User.objects.get(handle=handle)
	except Exception as e:
		return HttpResponse("This user handle does not belong to anyone!")
	else:
		users = []
		for user in User.objects.all():
			if(this_user in user.following.iterator()):
				users.append(user)
		users = '<br/><br/>'.join([str(user) for user in users])
		return HttpResponse(users)


def registration_success(request):
	if request.method == 'POST':
		# do registration stuff
		name = request.POST['fullname']
		handle = request.POST['handle']
		password = request.POST['pass']
		email_id = request.POST['email']
		dob = request.POST['dob']
		if request.POST['gender'] == 'male':
			gender = 'M'
		elif request.POST['gender'] == 'female':
			gender = 'F'
		else:
			gender = 'O'
		user = User(name=name, handle=handle, email_id=email_id, dob=dob, gender=gender, img=None, joined_on=timezone.now())
		# print(dob)
		user.save()
		# user_creds = UserLoginCredentials(user.uid)
	return render(request, 'registration/success.html')

def registration(request):
	return render(request, 'registration/index.html')
