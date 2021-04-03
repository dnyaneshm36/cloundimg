from django.shortcuts import render
from .KeySerializer import KeySerializer
from cripto.models import Key

import json

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import generics,mixins
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.



class KeysAPIView(mixins.CreateModelMixin,generics.ListAPIView): #crea te list 
    permission_classes        =[AllowAny]
    authentication_classes    =[]
    serializer_class          =KeySerializer

    def get_queryset(self):
        qs = Key.objects.all()
        query = self.request.GET.get('q')

        if query is not None:
            qs = qs.filter(content__icontains = query)
        return qs

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class KeysDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin , generics.RetrieveAPIView):
    permission_classes        =[IsAuthenticated]
    authentication_classes    =[BasicAuthentication]
    serializer_class          =KeySerializer
    
    queryset                   =Key.objects.all()

    def put(self, request, *args, **kwargs):
        return  self.update(request,*args,**kwargs)
    
    def patch(self, request, *args, **kwargs):
        return  self.partial_update(request,*args,**kwargs)

    def delete(self, request, *args, **kwargs):
        return  self.destroy(request,*args,**kwargs)
