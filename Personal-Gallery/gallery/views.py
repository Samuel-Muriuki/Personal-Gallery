from multiprocessing import context
from unicodedata import category
from django.shortcuts import render
from .models import Category, Image

# Create your views here.
def home_gallery(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'home.html', context)

def adding_photos(request):
    return render(request, 'gallery/adding_photos.html')

def viewing_photos(request, pk):
    return render(request, 'gallery/viewing_photos.html')