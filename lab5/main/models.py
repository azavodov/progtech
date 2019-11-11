from django.db import models


class Name(models.Model):
    name = models.CharField(max_length=10, unique=True, null=False, blank=False)

    def __str__(self):
        return f"{self.name}"

    def as_dict(self):
        return {
            "id": self.pk,
            "name": self.name,
        }


class Photo(models.Model):
    name = models.ForeignKey(Name, on_delete=models.CASCADE, null=False, blank=False)
    photo = models.URLField(max_length=2048, null=False, blank=False)

    def __str__(self):
        return f"{self.name} - {self.photo}"

    def as_dict(self):
        return {
            "id": self.pk,
            "name": self.name.as_dict(),
            "photo": self.photo,
        }
