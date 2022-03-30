from multiprocessing import context
from unicodedata import category
from django.shortcuts import render
from .models import Category, Image

# Create your views here.
def home_gallery(request):
    categories = Category.objects.all()
    images = Image.objects.all()
    context = {'categories': categories, 'images': images}
    return render(request, 'home.html', context)

def adding_photos(request):
    return render(request, 'gallery/adding_photos.html')

def viewing_photos(request, pk):
    image = Image.objects.get(id=pk)
    return render(request, 'gallery/viewing_photos.html', {'image': image})

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("catefory")
        searched_categories = Category.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'gallery/searching_photos.html', {"message": message, "category": searched_categories})

    else:
        message = "You haven't searched for any category"
        return render(request, 'gallery/searching_photos.html', {"message": message})