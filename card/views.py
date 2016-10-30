import datetime
from django.http import JsonResponse
from django.shortcuts import render

from SJTURD_Website import settings
from .models import Card


def card_list(request):
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
        'items_url': 'api/getCards',
    }

    return render(request, 'card/cardList.html', context)


def get_cards(request):
    MAX_DAY = 10

    data = {
        'data': [],
    }

    if not request.is_ajax():
        return JsonResponse(data)

    data = Card.objects.all().filter(paired=False)\
        .filter(date__gte=datetime.datetime.today() - datetime.timedelta(days=MAX_DAY)).order_by('-date')

    if len(data) == 0:
        data = {
            'data': [],
        }
        return JsonResponse(data)

    data = [{
                'id': str(i.pk),
                'student_id': i.student_id[:-3] + '***',
                'name': i.name,
                'lfoffice': i.lfoffice.name,
            }
            for i in data]

    data = {
        'data': data,
    }

    return JsonResponse(data)
