from django.urls import path, re_path
from . import views
from django.contrib.auth.views import (
    login, logout, password_reset, password_reset_done, password_reset_confirm,
    password_reset_complete
)


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', login, {'template_name': 'accounts/login.html'}, name='login'),
    path('logout/', logout, {'template_name': 'accounts/logout.html'}, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('change-password/', views.change_password, name='change_password'),
    path('reset-password/', password_reset,
        {'template_name': 'accounts/reset_password.html'},  name='reset_password'),
    path('reset-password/done/', password_reset_done, name='password_reset_done'),

    #example email host for debugging
    #python -m smtpd -n -c DebuggingServer localhost:1025
    #customize password reset template, example in medhacks
    re_path(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        password_reset_confirm, name='password_reset_confirm'),

    #customize password reset template, example in medhacks
    path('reset-password/complete/', password_reset_complete, name='password_reset_complete')

]
