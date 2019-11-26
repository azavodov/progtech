from datetime import datetime

import feedparser
from django.db import models


class Channel(models.Model):
    url = models.URLField(max_length=1024)
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.url

    def as_dict(self):
        return {
            "id": self.pk,
            "url": self.url,
            "name": self.name,
        }

    def fetch_feeds(self):
        feeds = feedparser.parse(self.url)
        for entry in feeds['entries']:
            if not len(Feed.objects.filter(link=entry['link'])):
                Feed.objects.create(
                    channel=self,
                    title=entry['title'],
                    link=entry['link'],
                    description=entry['summary'],
                    published_time=datetime(*(entry['published_parsed'][0:6])),
                )


class Feed(models.Model):
    channel = models.ForeignKey(Channel, blank=False, null=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=2000, blank=True, null=True)
    link = models.CharField(max_length=2000, unique=True)
    description = models.TextField(blank=True, null=True)
    published_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def as_dict(self):
        return {
            "id": self.pk,
            "channel_id": self.channel.pk,
            "title": self.title,
            "link": self.link,
            "description": self.description,
            "published_time": self.published_time,
        }
