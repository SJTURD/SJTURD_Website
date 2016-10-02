from django.http import JsonResponse
from django.shortcuts import render

from main.models import Category, Location


def index(request):
    return render(request, 'index.html')


def get_categories(request):
    data = Category.objects.all()
    data = [{'pk': cat.pk, 'name': cat.name} for cat in data]
    data = [{'pk': 0, 'name': '所有类别'}] + data

    data = {
        'data': data,
        'default': 0,
    }

    return JsonResponse(data)


def get_locations(request):
    data = Location.objects.all()
    data = [{'pk': loc.pk, 'name': loc.name} for loc in data]
    data = [{'pk': 0, 'name': '全部地点'}] + data

    data = {
        'data': data,
        'default': 0,
    }

    return JsonResponse(data)
