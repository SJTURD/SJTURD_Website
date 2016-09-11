from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

from .models import Found


def items(request):
    context = {
        'MEDIA_URL': settings.MEDIA_URL
    }

    return render(request, 'found/items.html', context)


def get_found_items(request):
    ITEMS_PER_PAGE = 10

    data = []

    if not request.is_ajax():
        return HttpResponse(serializers.serialize('json', data), content_type="application/json")

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
        return HttpResponse(serializers.serialize('json', data), content_type="application/json")

    if not page * ITEMS_PER_PAGE - ITEMS_PER_PAGE < len(data) <= page * ITEMS_PER_PAGE:
        page = (len(data) - 1) / ITEMS_PER_PAGE + 1

    data = data[page * ITEMS_PER_PAGE - ITEMS_PER_PAGE:page * ITEMS_PER_PAGE]

    return HttpResponse(serializers.serialize('json', data), content_type="application/json")