import datetime
import csv

from django.http import HttpResponse
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
                'student_id': i.student_id,
                'name': i.name,
                'lfoffice': i.lfoffice,
            }
            for i in data]

    data = {
        'data': data,
    }

    return JsonResponse(data)


def new_card(request):
    return render(request, 'card/newCard.html')


def upload_new_card(request):
    try:
        params = request.POST

        content = params['content']
        password = params['password']

        assert password == 'sillyPassword'

        f = open('tmp.csv', 'w')
        f.write(content)
        f.close()
        f = open('tmp.csv', 'r')
        csv_reader = csv.reader(f)
        content = list(csv_reader)
        f.close()

        for line in content:
            if len(line) == 3:
                new_object = Card(student_id=line[0], name=line[1], lfoffice_id=int(line[2]))
                new_object.save()

        return HttpResponse('Success.')

    except Exception as e:
        print(e)
        return HttpResponse('Failed.')
