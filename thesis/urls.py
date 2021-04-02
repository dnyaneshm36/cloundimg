from django.urls import path

from . import views
from django.conf.urls import url

urlpatterns = [
     path("hello", views.hello, name="index"),
     path("senderkeylc", views.senderAPIView.as_view(),name="senderkeycreate"),
     path("senderkeyrud/<int:pk>", views.SenderDetailAPIView.as_view(),name="senderkeyretrive"),
     path("receiverkeylc", views.ReceiverAPIView.as_view(),name="senderkeycreate"),
     path("receiverkeyrud/<int:pk>", views.ReceiverDetailAPIView.as_view(),name="senderkeyretrive"),
     # url(r'^senderkeyrud/(?P<pk>\d+)/$',SenderDetailAPIView.as_view(),name="senderkeyretrive" ),
]


# lc = list and create
# rud = reterive update and delete