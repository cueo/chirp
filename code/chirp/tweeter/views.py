from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse
from .models import *

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
			return HttpResponse('Login successful!')
		if(password == pwd):
			return HttpResponse('Invalid username and password combination!')

def user_profile(request, handle):
	try:
		user = User.objects.get(handle=handle)
	except Exception as e:
		return HttpResponse("This user handle does not belong to anyone!")
	else:
		tweets = Tweet.objects.all().filter(author=user).order_by('-ts')
		tweets = '<br/><br/>'.join([str(tweet) for tweet in tweets])
		return HttpResponse(tweets)

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
