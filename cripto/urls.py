from django.urls import path

from . import views
from django.conf.urls import url

urlpatterns = [
     path("keys", views.KeysAPIView.as_view(),name="keyscreate"),
     path("keygens", views.keygen,name="keygen"),
     path("keyshow", views.Keydisplay,name="keyshow"),
     path("publicupdate", views.uploadpublickey,name="uploadpublic"),
     path("check", views.checkcerrect,name="correct"),
     path("keys/<int:pk>", views.KeysDetailAPIView.as_view(),name="keysedit"),
     path('upload/', views.upload_file , name='upload'),
     path('search', views.trapdoorTest , name='search'),

     # path('play/', views.CreateAPIViewkeys.as_view() , name='play'),
     
]


# lc = list and create
# rud = reterive update and delete