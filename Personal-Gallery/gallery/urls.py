from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

# URL Configurations
urlpatterns = [
    path('', views.home_gallery, name = 'home'),
    path('add_photo', views.adding_photos, name = 'adding'),
    path('view_photo/<str:pk>/', views.viewing_photos, name = 'viewing')
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)