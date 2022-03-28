from django.urls import path
from . import views


# URL Configurations
urlpatterns = [
    path('', views.home_gallery, name = 'home'),
    path('add_photo', views.adding_photos, name = 'adding'),
    path('view_photo/<str:pk>/', views.viewing_photos, name = 'viewing')
]