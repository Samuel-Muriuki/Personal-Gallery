from django.urls import path
from . import views


# URL Configurations
urlpatterns = [
    path('home', views.home_gallery, name = 'home'),
    path('add_photo/<str:pk>/', views.adding_photos, name = 'adding'),
    path('view_photo', views.viewing_photos, name = 'viewing')
]