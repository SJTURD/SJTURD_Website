from django.http import JsonResponse
from django.shortcuts import render

from main.models import Category, Location, LFOffice
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


def lfoffice(request):
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
        'items_url': '/api/getLFOffices',
    }
    return render(request, 'main/lfoffice.html', context)


def get_lfoffices(request):
    data = {
        'data': [],
    }

    if not request.is_ajax():
        return JsonResponse(data)

    data = LFOffice.objects.all()

    if len(data) == 0:
        data = {
            'data': [],
        }
        return JsonResponse(data)

    data = [{
                'id': str(i.pk),
                'name': i.name,
                'location': i.detail,
                'contact': i.contact,
            }
            for i in data]

    data = {
        'data': data,
    }

    return JsonResponse(data)
