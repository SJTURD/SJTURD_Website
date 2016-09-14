from django.shortcuts import render, redirect
from django.conf import settings
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):
	return render(request, 'volunteer/index.html')

def login_view(request):
	# if request.user.is_authenticated:
	if True:
		return redirect('/volunteer/index')
	return render(request, 'volunteer/login.html')

# just a api, return message on whether it's logged in.
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    # user = authenticate(username=username, password=password)
    # if user is not None:
    if True:
        # login(request, user)
        return True
    else:
    	return False

# def retrieve_view(request):
	# acutally it's just the same as in LOST!
	# return redirect("/lost/?")
	# return render(request, "volunteer/retrieve.html")

def upload_view(request):
	context = {
		'MEDIA_URL': settings.MEDIA_URL
	}
	return render(request, "volunteer/upload.html", context)

def upload(request):
	catagory = request["POST"]["catagory"]
	location = request["POST"]["location"]
	imageUrl = request["POST"]["imageUrl"]
	if imageUrl == "":
		return False
	return True