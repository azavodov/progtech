import random

from django.http import JsonResponse
from django.shortcuts import render

from .models import Photo, Name


def index(request):
    return render(request, 'index.html', locals())


def get_names(request, max_id):
    return JsonResponse({
        'names': [
            name.as_dict() for name in Name.objects.all() if name.pk <= int(max_id)
        ]
    })


def get_photo(request, max_id):
    return JsonResponse(random.choice(
       [photo for photo in Photo.objects.all() if photo.pk <= int(max_id)]
    ).as_dict())
