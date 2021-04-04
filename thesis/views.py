from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
import json

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import generics,mixins
from rest_framework.views import APIView
from rest_framework.response import Response

from .ReceiverkeySerializer import ReceiverSerializer
from .SenderkeySerializer import SenderSerializer

from .models import Senderkey
from .models import Receiverkey
# Create your views here.


def hello(request):  
    data = {
        'bit' : 1024,
        'prime_number': "hello world"
    }
    data = json.dumps(data)
    return HttpResponse(data, content_type="application/json")

class senderAPIView(mixins.CreateModelMixin,generics.ListAPIView): #crea te list 
    permission_classes        =[AllowAny]
    authentication_classes    =[]
    serializer_class          =SenderSerializer

    def get_queryset(self):
        qs = Senderkey.objects.all()
        query = self.request.GET.get('q')

        if query is not None:
            qs = qs.filter(content__icontains = query)
        return qs

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class SenderDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin , generics.RetrieveAPIView):
    permission_classes        =[IsAuthenticated]
    authentication_classes    =[BasicAuthentication]
    serializer_class          =SenderSerializer
    
    queryset                   =Senderkey.objects.all()

    def put(self, request, *args, **kwargs):
        return  self.update(request,*args,**kwargs)
    
    def patch(self, request, *args, **kwargs):
        return  self.partial_update(request,*args,**kwargs)

    def delete(self, request, *args, **kwargs):
        return  self.destroy(request,*args,**kwargs)



class ReceiverAPIView(mixins.CreateModelMixin,generics.ListAPIView): #crea te list 
    permission_classes        =[AllowAny]
    authentication_classes    =[]
    serializer_class          =ReceiverSerializer

    def get_queryset(self):
        qs = Receiverkey.objects.all()
        query = self.request.GET.get('q')

        if query is not None:
            qs = qs.filter(content__icontains = query)
        return qs

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class ReceiverDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin , generics.RetrieveAPIView):
    permission_classes        =[IsAuthenticated]
    authentication_classes    =[BasicAuthentication]
    serializer_class          =ReceiverSerializer
    
    queryset                   =Receiverkey.objects.all()

    def put(self, request, *args, **kwargs):
        return  self.update(request,*args,**kwargs)
    
    def patch(self, request, *args, **kwargs):
        return  self.partial_update(request,*args,**kwargs)

    def delete(self, request, *args, **kwargs):
        return  self.destroy(request,*args,**kwargs)


# class SenderDetailAPIView(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Senderkey.objects.all()
#     serializer_class = SenderSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#     def patch(self, request, *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)




from .models import Uploaddata
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import cloudinary
import os
from cloudinary import uploader



from .form import UploaddataForm
from django.shortcuts import render, redirect
from thesis.form import UploaddataForm

def upload_file(request):
    form = UploaddataForm(request.POST, request.FILES)
    if form.is_valid():
        uploaded_img = form.save(commit=False)
        uploaded_img.data = form.cleaned_data['datafile'].file.read()
        
        uploaded_img.save()
        return redirect('/')
    else:
        form = UploaddataForm()
    return render(request, 'uploadfile.html', {'form': form})