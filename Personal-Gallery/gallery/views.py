from django.shortcuts import render

# Create your views here.
def home_gallery(request):
    return render(request, 'home.html')

def adding_photos(request, pk):
    return render(request, 'gallery/adding_photos.html')

def viewing_photos(request):
    return render(request, 'gallery/viewing_photos.html')