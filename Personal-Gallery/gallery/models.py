from unicodedata import category
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length= 30)

    def __str__(self):
        return self.name


class Location(models.Model):
    area = models.CharField(max_length=100)

    def __str__(self):
        return self.area


class Image(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    description = models.CharField(max_length=300, blank=False)
    image = models.CharField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.description