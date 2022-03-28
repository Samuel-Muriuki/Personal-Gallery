from django.shortcuts import render

# Create your views here.
def home_gallery(request):
    return render(request, 'gallery/home_gallery.html')

def adding_photos(request, primary_key):
    return render(request, 'gallery/adding_photos.html')

def viewing_photos(request):
    return render(request, 'gallery/viewing_photos.html')