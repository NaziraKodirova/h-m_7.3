from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=50)
    image = models.URLField()


class Albom(models.Model):
    title = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)
    cover = models.URLField()
    last_updated = models.DateTimeField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)

class Songs(models.Model):
    title = models.CharField(max_length=100)
    cover = models.URLField()
    albom = models.ForeignKey(Albom, on_delete=models.CASCADE, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)
