from django.urls import path

from . import views
from django.conf.urls import url

urlpatterns = [
     path("keys", views.KeysAPIView.as_view(),name="keyscreate"),
     path("keys/<int:pk>", views.KeysDetailAPIView.as_view(),name="keysedit"),
    
]


# lc = list and create
# rud = reterive update and delete