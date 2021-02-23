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

