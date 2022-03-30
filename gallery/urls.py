from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

# URL Configurations
urlpatterns = [
    path('', views.home_gallery, name = 'home'),
    path('search', views.search_results, name = 'searching'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)