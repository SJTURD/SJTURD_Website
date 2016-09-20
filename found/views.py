import json

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.conf import settings

from .models import Found
from main.models import Category, Location


def items(request):
    context = {
        'MEDIA_URL': settings.MEDIA_URL
    }

    return render(request, 'found/items.html', context)


def get_categories(request):
    data = Category.objects.all()
    data = [{'pk': cat['pk'], 'name': cat['fields']['name']} for cat in json.loads(serializers.serialize('json', data))]
    data = [{'pk': 0, 'name': 'ALL'}] + data

    data = {
        'data': data
    }

    return JsonResponse(data)


def get_locations(request):
    data = Location.objects.all()
    data = [{'pk': loc['pk'], 'name': loc['fields']['name']} for loc in json.loads(serializers.serialize('json', data))]
    data = [{'pk': 0, 'name': 'ALL'}] + data

    data = {
        'data': data
    }

    return JsonResponse(data)


def get_found_items(request):
    ITEMS_PER_PAGE = 10

    data = {
        'founds': [],
        'page': 1,
        'category': 0,
        'location': 0,
        'end_of_list': True,
    }

    if not request.is_ajax():
        return JsonResponse(data)

    params = request.GET

    page = int(params['page'])
    category = int(params['category'])
    location = int(params['location'])

    data = Found.objects.all().filter(paired=False).order_by('-date')
    if category > 0:
        data = data.filter(category=category)
    if location > 0:
        data = data.filter(location=location)

    if len(data) == 0:
        data = {
            'founds': [],
            'page': 1,
            'category': category,
            'location': location,
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

    data = {
        'founds': json.loads(serializers.serialize('json',
                                                   data[page * ITEMS_PER_PAGE - ITEMS_PER_PAGE:page * ITEMS_PER_PAGE])),
        'page': page,
        'category': category,
        'location': location,
        'end_of_list': end_of_list,
    }

    return JsonResponse(data)
