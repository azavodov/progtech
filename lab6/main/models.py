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
            "source_id": self.channel.pk,
            "title": self.title,
            "link": self.link,
            "description": self.description,
            "published_time": self.published_time,
        }
