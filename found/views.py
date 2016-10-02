import json

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.conf import settings

from .models import Found
from main.models import Category, Location


def item_list(request):
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
        'selector1_init_url': 'api/getCategories',
        'selector2_init_url': 'api/getLocations',
        'item_url': 'api/getItems',
    }

    return render(request, 'found/itemList.html', context)


def get_categories(request):
    data = Category.objects.all()
    data = [{'pk': cat['pk'], 'name': cat['fields']['name']} for cat in json.loads(serializers.serialize('json', data))]
    data = [{'pk': 0, 'name': '所有类别'}] + data

    data = {
        'data': data,
        'default': 0,
    }

    return JsonResponse(data)


def get_locations(request):
    data = Location.objects.all()
    data = [{'pk': loc['pk'], 'name': loc['fields']['name']} for loc in json.loads(serializers.serialize('json', data))]
    data = [{'pk': 0, 'name': '全部地点'}] + data

    data = {
        'data': data,
        'default': 0,
    }

    return JsonResponse(data)


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
    category = int(params['selector1_val'])
    location = int(params['selector2_val'])

    data = Found.objects.all().filter(paired=False).order_by('-date')
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
                'url': 'found/item?id=' + str(i.pk),
                'left_field': i.category.name,
                'right_field': str(i.date.date())[5:],
                'bottom_field': i.lfoffice.name,
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
