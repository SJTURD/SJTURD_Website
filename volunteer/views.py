from django.shortcuts import render, redirect
from django.conf import settings
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response 

from database.models import *
from django.template import RequestContext
from django import forms
from django.http import HttpResponse
import os

def index_init(request):
    request.session["logged"]=0
    return index(request)

def index(request):

    if request.session["logged"]==1:
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
        return render_to_response('volunteer/index.html',context)
    else:
        return render_to_response('volunteer/login.html',{})

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    tmp=Volunteer.objects.filter(name=username)
    error_message = {'message':"Wrong user or password!"}

    if len(tmp)>0:
        if tmp[0].password==password:
            request.session['logged']=1
            return index(request)
        else:
            return render_to_response('volunteer/login.html',error_message)
    else:
        return render_to_response('volunteer/login.html',error_message)


class UserForm(forms.Form):
    category = forms.CharField()
    description =forms.CharField()
    owner=forms.CharField()
    contact=forms.CharField()
    img = forms.FileField()

def upload_view(request):
    if request.method == "POST":
        uf = UserForm(request.POST,request.FILES)
        if uf.is_valid():
            item=LostItem()
            item.item_id= len(LostItem.objects.all())+1
            item.category = uf.cleaned_data['category']
            item.description =uf.cleaned_data['description']
            item.owner=uf.cleaned_data['owner']
            item.contact=uf.cleaned_data['contact']
            item.img = uf.cleaned_data['img']
            item.save()
            os.rename(item.img.path,settings.MEDIA_ROOT+"/lost/"+str(len(LostItem.objects.all()))+".jpg")
            item.save()
            return HttpResponse(item.img.path)
    else:
         uf = UserForm()
    return render_to_response('volunteer/upload.html',{'uf':uf})


def upload(request):
    catagory = request["POST"]["catagory"]
    location = request["POST"]["location"]
    imageUrl = request["POST"]["imageUrl"]
    if imageUrl == "":
        return False
    return True
