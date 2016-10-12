import os

from django.shortcuts import render, redirect
from django.conf import settings
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.shortcuts import render_to_response 
from django.template import RequestContext
from django import forms
from django.http import HttpResponse

from django.contrib.auth.models import User
from found.models import Found
from main.models import Category, Location


def index_init(request):
    request.session["logged"]=0
    return index(request)

def index(request):

    if request.session["logged"]==1:
        context={}
        context['numLostItem']=len(Found.objects.all())
        context['rangeNumLostItem']=range(context['numLostItem'])
        context['lostItem']={}
        for i in Found.objects.all():
            index=i.pk
            context['lostItem'][index]={}
            context['lostItem'][index]['id']=i.pk
            context['lostItem'][index]['src']="/media/"+i.picture.name
            context['lostItem'][index]['catagory']=i.category
            context['lostItem'][index]['description']=i.detail
            context['lostItem'][index]['lostTime']=i.date
            # context['lostItem'][index]['owner']=i.owner
            context['lostItem'][index]['contact']=i.phone
            context['lostItem'][index]['status']=i.paired
        context['lostItemValues']=context['lostItem'].values()
        return render_to_response('volunteer/index.html',context)
    else:
        return render_to_response('volunteer/login.html',{})

def login(request):
    username = request.POST.get('username',False) #Post[] -> Post.get(,False)
    password = request.POST.get('password',False)
    tmp=User.objects.filter(username=username)


    if len(tmp)>0:
        if tmp[0].is_staff:
            if check_password(password,tmp[0].password):
                request.session['logged'] = 1
                return index(request)
            else:
                error_message = {'message': "Wrong password!"}
                return render_to_response('volunteer/login.html', error_message)
        else:
            error_message = {'message': "Permission denied!"}
            return render_to_response('volunteer/login.html', error_message)
    else:
        error_message = {'message': "User does not exist!"}
        return render_to_response('volunteer/login.html',error_message)

# upload part
class UserForm(forms.Form):
    CATEGORY_LIST=(
        (1,"第一分类"),
        (2,"第二分类"),
        (3,"第三分类")
    )
    category = forms.IntegerField(widget=forms.Select(choices=CATEGORY_LIST))
    LOCATION_LIST=(
        (1,"第一地点"),
        (2,"第二地点"),
        (3,"第三地点")
    )
    location = forms.IntegerField(widget=forms.Select(choices=LOCATION_LIST))
    description = forms.CharField(label="描述")
    # owner=forms.CharField(label="物主")
    contact=forms.CharField(label="联系方式")
    img = forms.FileField(label="图片")

def upload_view(request):
    if request.method == "POST":
        uf = UserForm(request.POST,request.FILES)
        if uf.is_valid():
            item=Found()
            item.category=Category.objects.get(id=uf.cleaned_data['category'])
            # item.location=Category.objects.get(id=uf.cleaned_data['location'])
            item.detail =uf.cleaned_data['description']
            # item.owner=uf.cleaned_data['owner']
            item.phone=uf.cleaned_data['contact']
            item.picture = uf.cleaned_data['img']
            item.save()
            # os.rename(item.img.path,settings.MEDIA_ROOT+"/lost/"+str(len(Lost.objects.all()))+".jpg")
            # item.save()
            uf=UserForm()
            message="Upload Completed!"
    else:
        uf = UserForm()
        message=""
    return render_to_response('volunteer/upload.html',{'uf':uf, 'message':message})

# retrieve part
def retrieve(request):
    retrieveList=request.POST.getlist('retrieveCheckBox')
    for i in retrieveList:
        a=Found.objects.get(pk=i)
        a.paired=1
        a.save()
    return index(request)
