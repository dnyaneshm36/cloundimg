from django.shortcuts import render
from django.contrib import messages
from .KeySerializer import KeySerializer,PublicKeySerializer
from cripto.models import Key

import json

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import generics,mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
# Create your views here.

from rest_framework import generics, status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse

def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid


class SenderAPIView(generics.RetrieveAPIView):
    serializer_class = KeySerializer
    permission_classes        =[]
    authentication_classes    =[]
    def get_object(self):
        request             =self.request
        if not is_json(request.body):
            data = {
                "details_error": "send data in json format"
            }
            data = json.dumps(data)
            return HttpResponse(data, content_type="application/json")   ##return has not thing
        bodydata                = json.loads(request.body)
        pku1body                = bodydata['pku1']
        pku2body                = bodydata['pku2']

        try:

            qs = get_object_or_404(Key.objects.filter(pku1 = pku1body))
            qs = get_object_or_404(Key.objects.filter(pku2 = pku2body))
            print(qs)
        except User.DoesNotExist:
            qs = get_object_or_404(Key.objects.filter(pku1 = pku1body))
        if qs == None:
            data ={ 
                "details_error": "public keys are not matched. "
            }
            return HttpResponse(data, content_type="application/json") 
        return qs

class ReceiverAPIView(generics.RetrieveAPIView):
    serializer_class = KeySerializer
    permission_classes        =[]
    authentication_classes    =[]
    passed_email              =None

    def get_object(self):
        request             =self.request
        passed_email        =request.GET.get('email',None) or self.passed_email

        try:
            user = get_object_or_404(User.objects.filter(email = passed_email))

            qs = get_object_or_404(Key.objects.filter(userid = user))
            # print(qs)
        except User.DoesNotExist:
            qs = get_object_or_404(User.objects.filter(email = passed_email))
        return qs

class UpdatePublickeysapi(APIView):
     #crea te list 
    def post(self, request, format=None):
        serializer = PublicKeySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


from .form import UploaddataForm
from django.shortcuts import render, redirect
from cripto.form import UploaddataForm
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import User
from django.http import Http404
def finds_social_account(request):
    user = request.user
    qs = SocialAccount.objects.all()
    qs = qs.filter(user__exact = user)
    if qs is not None:
        print("socoal acuunfot find")
        raise Http404("Login with google use service. ")
    return qs
    
def upload_file(request):
    form = UploaddataForm(request.POST, request.FILES)
    # print(request.user)
    # social = finds_social_account(request)
    if form.is_valid():
        uploaded_img = form.save(commit=False)
        uploaded_img.file = form.cleaned_data['datafile'].file.read()
        uploaded_img.userid = request.user
        uploaded_img.save()
        messages.error(request, ('Successfully added file .'))
        return redirect('upload/')
    else:
        messages.error(request, ('Fail to upload .'))
        form = UploaddataForm()
    return render(request, 'uploadfileword.html', {'form': form})


from django.http import HttpResponse
import json
import requests

def keygen(request,*args,**kwargs):
    user = request.user
    if user is None:
        messages.error(request, ('Login First.'))
        return redirect("/")
    qs = Key.objects.all()
    qs = qs.filter(userid__exact = user)
    if len(qs)>0:
        messages.warning(request, ('Key are aleardy Genrated.'))
        return redirect("/clpeks/keyshow")
    else:

        LOCALHOST = "http://localhost:8080/"
        CYTOPTO_HEROKU = "https://criptography-dnyanesh.herokuapp.com/"

        ENDPOINT = CYTOPTO_HEROKU
        headers = {
            "Content-Type": "application/json"
        }
        Requestdata = ""
        # r = requests.get(ENDPOINT+"microservice/clpeks/setup",data=json.dumps(Requestdata),headers= headers)
        # Responddata = r.json()
        # p = Responddata['p']
        # master_key_lambda = Responddata['master_key_lamda']
        # PKc = Responddata["pkc"]
        user = request.user
        mail = user.email
        uid  = user.id
        x = mail.find("@")
        uname = user.username
        userid = uname + mail[0:x]
        r = requests.get(ENDPOINT+"microservice/clpeks/ePPK/"+userid,data=json.dumps(Requestdata),headers= headers)
        # print(r)
        Responddata = r.json()
        # print(Responddata)
        Qu = Responddata["qu"]
        Du = Responddata["du"]

        r = requests.get(ENDPOINT+"microservice/clpeks/sSV",data=json.dumps(Requestdata),headers= headers)
        # print(r)
        Responddata = r.json()
        # print(Responddata)

        
        Requestdata={
               "userid": uid,
            "clientId":userid,
            "qu": Qu,
            "du": Du
            }

        # print(json.dumps(Requestdata))
        query_params_copy =json.dumps(Requestdata)
        sdata = json.loads(query_params_copy)
        serializer = KeysAPIView.serializer_class(data=sdata)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        # host = request.get_host()
        # endpoint = str(host)+"/clpeks/play/"
        # r = requests.get(endpoint,data=json.dumps(Requestdata),headers= headers,params=request.GET)
        # r= str(r)
        data = {
            "resopnce":r,
        'generate': "already keys generated",
        'key': True}
    

    return HttpResponse(data, content_type="application/json")    

from .form import keysFormid
from .models import Key
from django.forms import modelform_factory

def Keydisplay(request, *args, **kwargs):
    form = keysFormid(request.POST )
    User = request.user.id
    if User is None:
        messages.error(request, ('Login First.'))
        return redirect("/")
    userkeys = Key.objects.filter(userid_id__exact=User)
    if len(userkeys)>0:
        form = keysFormid(instance=userkeys[0])
        formhtml = keysFormid(request.POST )
        if formhtml.is_valid():
            print(formhtml)
        render(request, 'keys.html', {'form': form})
    else:
        r = keygen(request)
        if(r.status_code == 201):
            userkeys = Key.objects.filter(userid_id__exact=User)[0]
            form = keysFormid(instance=userkeys)
    return render(request, 'keys.html', {'form': form})


from .form import  KeyFormpublic,KeyForm
from rest_framework.generics import get_object_or_404
    
def uploadpublickey(request,*args,**kwargs):
    form = KeyFormpublic(request.POST )
    User = request.user.id
    if User is None:
        messages.error(request, ('Login First.'))
        return redirect("/")
    if form.is_valid():
        userkeys = Key.objects.filter(userid_id__exact=User)[0]
        if userkeys.pku1 == None or userkeys.pku1 =='None':
            userkeys.pku1 = form.cleaned_data["pku1"]
            userkeys.pku2 = form.cleaned_data["pku2"]
            userkeys.save()
            messages.error(request, ('public are updated 👍 showing keys.'))
        else:
            messages.error(request, (' 🤟 public showing keys. 🤟'))

        form = KeyForm(instance=userkeys)
        return render(request, 'keys.html', {'form': form})
    else: 
        form = KeyFormpublic()
    return render(request, 'keys.html', {'form': form})

def checkcerrect(request,*args,**kwargs):
    User = request.user.id
    userkeys = Key.objects.filter(userid_id__exact=User)[0]
    CYTOPTO_HEROKU = "https://criptography-dnyanesh.herokuapp.com/"

    ENDPOINT = CYTOPTO_HEROKU
    headers = {
        "Content-Type": "application/json"
    }

    if userkeys.pku1 == None:
        messages.error(request, (' update Public keys first. \n'))
        form = KeyForm(instance=userkeys)
        return render(request, 'keys.html', {'form': form})

    Requestdata={
        "pkr1":userkeys.pku1,
        "pkr2":userkeys.pku2
    } 
    r = requests.get(ENDPOINT+"microservice/clpeks/pairingcheck",data=json.dumps(Requestdata),headers= headers)
    print(r)
    Responddata = r.json()
    print(Responddata)
    if Responddata['checked']:
         messages.error(request, (' ✔ Public keys are correct. ✔ \n'+Responddata['description']))
    else:
        messages.error(request, (' ❌ public showing keys. ❌  \n' +Responddata['description']))
    form = KeyForm(instance=userkeys)
    return render(request, 'keys.html', {'form': form})

def trapdoorTest(request,*args,**kwargs):
    return render(request, 'search.html')
