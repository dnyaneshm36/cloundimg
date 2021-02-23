from django.urls import path,include
from django.views.generic.base import TemplateView
from socialmodule import views
from socialmodule.views import ProfileView,DataDeletionView
urlpatterns = [
    # path('', TemplateView.as_view(template_name='index.html')),
    # path('profile/',
    #      TemplateView.as_view(template_name='profile.html')),
     path('accounts/profile/',ProfileView.as_view() ),
     path('deauthtication/',DataDeletionView.as_view(), name="deauthtication"),
    #  path('accounts/profile/',views.Profile,name="profile" )
]
