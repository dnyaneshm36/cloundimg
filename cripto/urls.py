from django.urls import path

from . import views
from django.conf.urls import url

urlpatterns = [
     path("keys", views.KeysAPIView.as_view(),name="keyscreate"),
     path("keygens", views.keygen,name="keygen"),
     path("keyshow", views.Keydisplay,name="keyshow"),
     path("keys/<int:pk>", views.KeysDetailAPIView.as_view(),name="keysedit"),
     path('upload/', views.upload_file , name='upload'),
     path('play/', views.CreateAPIViewkeys.as_view() , name='play'),
     
]


# lc = list and create
# rud = reterive update and delete