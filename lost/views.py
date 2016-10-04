import json

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.conf import settings

from .models import Lost
from main.models import Category, Location


def item_list(request):
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
        'selector1_init_url': '/main/api/getCategories',
        'selector2_init_url': '/main/api/getLocations',
        'items_url': 'api/getItems',
    }

    return render(request, 'lost/itemList.html', context)


def get_items(request):
    ITEMS_PER_PAGE = 10

    data = {
        'data': [],
        'page': 1,
        'selector1_val': 0,
        'selector2_val': 0,
        'end_of_list': True,
    }

    if not request.is_ajax():
        return JsonResponse(data)

    params = request.GET

    page = int(params['page'])
    category = int(params['category'])
    location = int(params['location'])

    data = Lost.objects.all().filter(paired=False).order_by('-date')
    if category > 0:
        data = data.filter(category=category)
    if location > 0:
        data = data.filter(location=location)

    if len(data) == 0:
        data = {
            'data': [],
            'page': 1,
            'selector1_val': category,
            'selector2_val': location,
            'end_of_list': True,
        }
        return JsonResponse(data)

    if page <= 0:
        page = 1

    if len(data) <= page * ITEMS_PER_PAGE - ITEMS_PER_PAGE:
        page = (len(data) - 1) / ITEMS_PER_PAGE + 1

    end_of_list = False
    if page * ITEMS_PER_PAGE - ITEMS_PER_PAGE < len(data) <= page * ITEMS_PER_PAGE:
        end_of_list = True

    data = [{
                'img': i.picture.name,
                'url': 'item?id=' + str(i.pk),
                'left_field': i.category.name,
                'right_field': str(i.date.date())[5:],
                'bottom_field': i.location.name,
            }
            for i in data]

    data = {
        'data': data[page * ITEMS_PER_PAGE - ITEMS_PER_PAGE:page * ITEMS_PER_PAGE],
        'page': page,
        'selector1_val': category,
        'selector2_val': location,
        'end_of_list': end_of_list,
    }

    return JsonResponse(data)


def item(request):
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
        'item_url': 'api/getItem',
    }

    return render(request, 'lost/item.html', context)


def get_item(request):
    data = {
        'img': '',
        'detail': [],
    }

    if not request.is_ajax():
        return JsonResponse(data)

    params = request.GET

    id = int(params['id'])

    try:
        data = Lost.objects.get(pk=id)
    except ObjectDoesNotExist:
        return JsonResponse(data)

    data = {
        'id': data.pk,
        'img': data.picture.name,
        'key': ['类别', '发现地点', '详细说明', '现所在地'],
        '类别': data.category.name,
        '发现地点': data.location.name,
        '详细说明': data.detail,
        '现所在地': data.lfoffice.name,
    }

    return JsonResponse(data)


def new_lost(request):
    category = Category.objects.all().order_by("name")
    location = Location.objects.all().order_by("name")
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
        'location' : location,
        'category' : category
    }
    return render(request, 'lost/newLost.html', context)


def search(request):
    location = request.GET['location']
    category = request.GET['category']
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
        'location' : location,
        'category' : category
    }
    return render(request, 'lost/checklist.html', context)


def upload_lost_item(request):
    category = Category.objects.all().order_by("name")
    location = Location.objects.all().order_by("name")
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
        'location' : location,
        'category' : category
    }
    return render(request, 'lost/uploadLostItem.html', context)

def upload(request):
    location = request.GET['location'];
    category = request.GET['category'];
    email = request.GET['email'];
    phone = request.GET['phone'];
    remark = request.GET['remark'];
    Lost.objects.create(user='999999',category=category,location=location,phone=phone,email=email,remark=remark)
    return render(request, 'lost/uploadResult.html')
