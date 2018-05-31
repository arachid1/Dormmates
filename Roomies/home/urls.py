from django.urls import path, include, re_path
from home.views import HomeView, ApplicationView, FavView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('favorites/', FavView.as_view(), name='favorites'),
    path('questions/', ApplicationView.as_view(), name='questions'),
    re_path(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/', views.change_friends,
    name='change_friends'),
    re_path(r'^questions/(?P<pk>\d+)/', views.view_profile_form, name='view_profile_form_with_pk'),

]
