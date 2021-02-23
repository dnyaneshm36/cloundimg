from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
     path("", views.index, name="index"),
     path('about/', views.about , name='about'),
     path('contact/', views.contact , name='contact'),
     path('upload/', views.upload_file , name='upload'),
     path('accounts/login/', views.upload_file , name='auth'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)