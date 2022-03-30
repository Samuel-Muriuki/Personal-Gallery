from multiprocessing import context
from unicodedata import category
from django.shortcuts import render
from .models import Category, Image, Location

# Create your views here.
def home_gallery(request):

    # category = request.GET.get('category')
    # print('category:', category)
    # if category != None:
    #     images = Image.objects.filter(category__name=category)
    # else:
    #     images = Image.objects.all()

    location = request.GET.get('location')
    print('location:', location)
    if location == None:
        images = Image.objects.all()
    else:
        images = Image.objects.filter(location__area=location)


    categories = Category.objects.all()
    # images = Image.objects.all()
    locations = Location.objects.all()
    context = {'categories': categories, 'images': images, 'locations': locations}


    return render(request, 'home.html', context)

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("catefory")
        searched_categories = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request, 'gallery/searching_photos.html', {"message": message, "category": searched_categories})

    else:
        message = "You haven't searched for any category"
        return render(request, 'gallery/searching_photos.html', {"message": message})