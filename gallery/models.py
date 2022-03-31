from unicodedata import category
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length= 30)

    def __str__(self):
        return self.name

    @classmethod
    def search_by_category(cls, search_term):
        category = cls.objects.filter(name__icontains=search_term)
        return category


class Location(models.Model):
    area = models.CharField(max_length=100)

    def __str__(self):
        return self.area


class Image(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    description = models.TextField(max_length=300, blank=False)
    # image = models.ImageField(max_length=500, null=False, blank=False)
    image = CloudinaryField('image')

    def __str__(self):
        return self.description

    def save_image(self):
        self.save()

    @classmethod
    def delete_image(cls,id):
        image = cls.objects.filter(id = id)
        image.delete()

    @classmethod
    def search_image(cls,search_term):
        image = cls.objects.filter(category__category__icontains= search_term)
        return image