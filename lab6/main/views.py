from django.http import JsonResponse
from django.shortcuts import render

from .models import Channel, Feed


def index(request):
    return render(request, 'index.html', locals())


def get_channels(request):
    return JsonResponse({'sources': [
        c.as_dict() for c in Channel.objects.all()
    ]})


def get_feeds(request):
    channel_id = request.GET.get('c_id')
    offset = int(request.GET.get('offset', 0))
    count = int(request.GET.get('count', 10))

    feeds = Feed.objects.filter(channel__id=channel_id) if channel_id else Feed.objects.all()
    feeds = list(feeds)[offset: offset+count]

    return JsonResponse({
        'feeds': [f.as_dict() for f in feeds],
    })
