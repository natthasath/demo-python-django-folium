from django.db import models

# Create your models here.

class focus(models.Model):
    name = models.CharField(max_length=50)
    latitude = models.FloatField(max_length=20)
    longitude = models.FloatField(max_length=20)
    show = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class group(models.Model):
    name = models.CharField(max_length=50)
    show = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class location(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    url = models.URLField(max_length=200, blank=True)
    group = models.ForeignKey(group, on_delete=models.CASCADE)
    latitude = models.FloatField(max_length=20)
    longitude = models.FloatField(max_length=20)

    def __str__(self):
        return self.name