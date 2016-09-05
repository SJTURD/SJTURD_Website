from django.shortcuts import render
from .models import Found


def items(request):
    found_items = Found.objects.filter(paired=False).order_by('-date')

    context = {
        'found_items': found_items,
    }

    return render(request, 'found/items.html', context)
