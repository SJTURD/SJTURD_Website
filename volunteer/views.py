from django.shortcuts import render, redirect
from django.conf import settings
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response 

from database.models import *
from django.template import RequestContext



def index(request):
    if 'username' not in request.session:
        return login_view(request)
    q=Volunteer.objects.get(volunteer_id=1)
    request.session['aaa']='username' in request.session
    return render_to_response('volunteer/index.html',{"aaa":request.session['aaa']})


def login_view(request):
    # if request.user.is_authenticated:
    # if True:
        # return redirect('/volunteer/index',{'aaa':1})
    return render_to_response('volunteer/login.html',{"aaa":'1'})
    # return render(request, 'volunteer/login.html')


# just a api, return message on whether it's logged in.
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    # user = authenticate(username=username, password=password)
    # if user is not None:
    # if True:
        # login(request, user)
    error_message = {'message':"Wrong user or password!"}
    context={}
    context['numLostItem']=len(LostItem.objects.all())
    context['rangeNumLostItem']=range(context['numLostItem'])
    context['lostItem']={}
    for i in LostItem.objects.all():
        index=i.item_id
        context['lostItem'][index]={}
        context['lostItem'][index]['id']=i.item_id
        context['lostItem'][index]['src']="/media/lost/"+str(i.item_id)+".jpg"
        context['lostItem'][index]['catagory']=i.category
        context['lostItem'][index]['description']=i.description
        context['lostItem'][index]['lostTime']=i.lost_time
        context['lostItem'][index]['owner']=i.owner
        context['lostItem'][index]['contact']=i.contact
        context['lostItem'][index]['status']=i.status
    context['lostItemValues']=context['lostItem'].values()
    context['ii']={}
    context['ii']['ok']="/media/lost/1.jpg"
    context['kk']=1

    tmp=Volunteer.objects.filter(name=username)
    if len(tmp)>0:
        if tmp[0].password==password:
            return render_to_response('volunteer/index.html',context)
        else:
            return render_to_response('volunteer/login.html',error_message)
    else:
        return render_to_response('volunteer/login.html',error_message)
        # return HttpResponseRedirect('/')
    # else:
        # return False

    # def retrieve_view(request):
    # acutally it's just the same as in LOST!
    # return redirect("/lost/?")
    # return render(request, "volunteer/retrieve.html")


def upload_view(request):
    context = {
        'MEDIA_URL': settings.MEDIA_URL
    }
    return render(request, "volunteer/upload.html", {"aaa":request.session['aaa']})


def upload(request):
    catagory = request["POST"]["catagory"]
    location = request["POST"]["location"]
    imageUrl = request["POST"]["imageUrl"]
    if imageUrl == "":
        return False
    return True
