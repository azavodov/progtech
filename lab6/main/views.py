from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.http import JsonResponse
from django.shortcuts import render

from .models import Channel, Feed


def index(request):
    return render(request, 'index.html', locals())


def get_channels(request):
    return JsonResponse({'channels': [
        c.as_dict() for c in Channel.objects.all()
    ]})


def add_channels(request):
    url = request.GET.get('url', None)
    name = request.GET.get('name', None)

    if url is None or name is None:
        return JsonResponse({'status': 'One of the fields is None'})

    try:
        val = URLValidator()
        val(url)
    except ValidationError as e:
        return JsonResponse({'status': 'Incorrect url'})

    Channel.objects.create(
        name=name,
        url=url,
    )

    return JsonResponse({'status': 'OK'})


def get_feeds(request):
    channel_id = request.GET.get('c_id')
    offset = int(request.GET.get('offset', 0))
    count = int(request.GET.get('count', 10))

    channel = Channel.objects.get(id=channel_id)
    channel.fetch_feeds()

    feeds = Feed.objects.filter(channel=channel) if channel_id else Feed.objects.all()
    feeds = list(feeds)[offset: offset+count]

    return JsonResponse({
        'feeds': [f.as_dict() for f in feeds],
    })
