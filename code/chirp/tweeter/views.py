from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse
from .models import *

def index(request):
    return HttpResponse("Chirp! This page is currently under development. Please come back later! :)")

def user_profile(request, handle):
    try:
        user = User.objects.get(handle=handle)
    except Exception as e:
        return HttpResponse("This user handle does not belong to anyone!")
    else:
        tweets = Tweet.objects.all().filter(author=user)
        tweets = '<br/><br/>'.join([str(tweet) for tweet in tweets])
        return HttpResponse(tweets)
