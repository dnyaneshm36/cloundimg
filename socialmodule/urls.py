from django.urls import path,include
from django.views.generic.base import TemplateView
from socialmodule import views
from socialmodule.views import ProfileView,DataDeletionView,Privacypolicy
urlpatterns = [
    # path('', TemplateView.as_view(template_name='index.html')),
    # path('profile/',
    #      TemplateView.as_view(template_name='profile.html')),
     path("",ProfileView.as_view(),name="home"),
     path('accounts/profile/',ProfileView.as_view() ),
     path('deauthtication/',DataDeletionView.as_view(), name="deauthtication"),
     path('privacypolicy/',Privacypolicy , name="privacypolicy"),
    #  path('accounts/profile/',views.Profile,name="profile" )
]


# https://www.freeprivacypolicy.com/live/67edc159-9c90-4c80-904f-6fca142dade9
# privacy polcicy list