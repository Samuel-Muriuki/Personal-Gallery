from django.urls import path
from . import views


# URL Configurations
urlpatterns = [
    path('', views.home_gallery, name = 'home_gallery'),
    path('add_photo/<str:pk>/', views.adding_photos, name = 'adding_photos'),
    path('view_photo', views.viewing_photos, name = 'viewing_photos')
]