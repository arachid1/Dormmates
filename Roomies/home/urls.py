from django.urls import path, include, re_path
from home.views import HomeView, ApplicationView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('questions/', ApplicationView.as_view(), name='questions'),
    re_path(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/', views.change_friends,
    name='change_friends'),

]
