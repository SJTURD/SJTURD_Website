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
    ITEMS_PER_PAGE = 100

    data = {
        'data': [],
        'page': 1,
        'end_of_list': True,
    }

    if not request.is_ajax():
        return JsonResponse(data)

    params = request.GET

    page = int(params['page'])
    data = Card.objects.all().filter(paired=False).order_by('-date')

    if len(data) == 0:
        data = {
            'data': [],
            'page': 1,
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
                'id': str(i.pk),
                'student_id': i.student_id[:-3] + '***',
                'name': i.name,
                'lfoffice': i.lfoffice.name,
            }
            for i in data]

    data = {
        'data': data[page * ITEMS_PER_PAGE - ITEMS_PER_PAGE:page * ITEMS_PER_PAGE],
        'page': page,
        'end_of_list': end_of_list,
    }

    return JsonResponse(data)
