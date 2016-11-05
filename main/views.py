import json

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
        'items_url': 'api/getLFOffices-2',
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


def get_lfoffices_2(request):
    data = '''
    [
        { "id": "1", "location": "一餐一楼服务台", "remark": "11:30-12:30；17:30-18:30" },
        { "id": "2", "location": "二餐内餐卡办理处", "remark": "11:30-12:30；17:30-18:30" },
        { "id": "3", "location": "三餐一楼交大吃吃", "remark": "11:30-12:30；17:30-18:30" },
        { "id": "4", "location": "四餐一楼交大吃吃", "remark": "11:30-12:30；17:30-18:30" },
        { "id": "5", "location": "五餐二楼学生餐厅门口", "remark": "11:30-12:30；17:30-18:30" },
        { "id": "6", "location": "哈乐餐厅刷卡处", "remark": "10:30-19:00" },
        { "id": "7", "location": "东上二楼小卖部", "remark": "10：00-14:3" },
        { "id": "8", "location": "东中2-203旁管理室", "remark": "8:00-17：30" },
        { "id": "9", "location": "东下一楼小卖部", "remark": "8:00-16:00" },
        { "id": "10", "location": "光彪楼一楼楼梯处", "remark": "12:00-21:00" },
        { "id": "11", "location": "光标楼二楼桌游区", "remark": "16:00-21:00" },
        { "id": "12", "location": "下院311", "remark": "14：00-17：00" },
        { "id": "13", "location": "致远游泳馆前台", "remark": "10:00-21:00" },
        { "id": "14", "location": "逸夫楼一楼值班处", "remark": "12:00-17:00；18:00-22:00" },
        { "id": "15", "location": "南体内场馆102", "remark": "10:00-20:30" },
        { "id": "16", "location": "一餐浴室一楼", "remark": "16:00-22:30" },
        { "id": "17", "location": "爱心屋", "remark": "10:00-20:00" },
        { "id": "18", "location": "思源门爱心亭", "remark": "10:00-17:00" },
        { "id": "19", "location": "保卫处老行政楼", "remark": "10:00-17:30" },
        { "id": "20", "location": "包图一楼值班台", "remark": "10:00-17:00" },
        { "id": "21", "location": "包图一楼保安台", "remark": "10:00-22:00" },
        { "id": "22", "location": "新图保安室", "remark": "10:00-20:00" },
        { "id": "23", "location": "陈瑞球楼一楼物业室", "remark": "10:00-22:00" },
        { "id": "24", "location": "二餐外现金充值处", "remark": "工作日：15：30-17：30  周末：10：30-14：00" },
        { "id": "25", "location": "一餐外现金充值处", "remark": "工作日：15：30-17：30  周末：10：30-14：00" }
    ]'''

    data = {
        'data': json.load(data),
    }

    return JsonResponse(data)
