from django.http import JsonResponse
from django.shortcuts import render

from main.models import Category, Location
from django.conf import settings


def index(request):
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
        'selector1_init_url': '/main/api/getCategories',
        'selector2_init_url': '/main/api/getLocations',
    }
    return render(request, 'index.html', context)


def get_categories(request):
    data = Category.objects.all().order_by('-pk')
    data = [{'pk': cat.pk, 'name': cat.name} for cat in data]
    data = [{'pk': 0, 'name': '所有类别'}] + data

    data = {
        'data': data,
        'default': 0,
    }

    return JsonResponse(data)


def get_locations(request):
    data = Location.objects.all().order_by('-pk')
    data = [{'pk': loc.pk, 'name': loc.name} for loc in data]
    data = [{'pk': 0, 'name': '全部地点'}] + data

    data = {
        'data': data,
        'default': 0,
    }

    return JsonResponse(data)
