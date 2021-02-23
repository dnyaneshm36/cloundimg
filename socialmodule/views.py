from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
# Create your views here.

from allauth.socialaccount.models import  SocialAccount

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    # def get(self, request, *args, **kwargs):
    #     print(request)
    #     return self.post(request, *args, **kwargs)

def Profile(request):
    return render(request, "profile.html")

from django.utils.decorators import method_decorator

import base64
import hashlib
import hmac
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
@method_decorator(csrf_exempt, name='dispatch')
class DataDeletionView(View):
    
    def post(self, request, *args, **kwargs):
        try:
            signed_request = request.POST['signed_request']
            encoded_sig, payload = signed_request.split('.')
        except (ValueError, KeyError):
            return HttpResponse(status=400, content='Invalid request')
 
        try:
            decoded_payload = base64.urlsafe_b64decode(payload + "==").decode('utf-8')
            decoded_payload = json.loads(decoded_payload)
 
            if type(decoded_payload) is not dict or 'user_id' not in decoded_payload.keys():
                return HttpResponse(status=400, content='Invalid payload data')
 
        except (ValueError, json.JSONDecodeError):
            return HttpResponse(status=400, content='Could not decode payload')
 
        try:
            secret = 'your own app secret key'
 
            sig = base64.urlsafe_b64decode(encoded_sig + "==")
            expected_sig = hmac.new(bytes(secret, 'utf-8'), bytes(payload, 'utf-8'), hashlib.sha256)
        except:
            return HttpResponse(status=400, content='Could not decode signature')
 
        if not hmac.compare_digest(expected_sig.digest(), sig):
            return HttpResponse(status=400, content='Invalid request')
 
        user_id = decoded_payload['user_id']
 
        try:
            # now you get facebook user id. you can delete its details from your database like below.
            user_account = FacebookUserModel.objects.filter(fb_userid=user_id).delete()
        except FacebookLoginDetails.DoesNotExist:
            return HttpResponse(status=200)
 
        # Own custom logic here
 
        return HttpResponse(status=200)