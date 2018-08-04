from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Roomies import views

urlpatterns = [
    path('', views.login_redirect, name='login_redirect'),
    path('admin/', admin.site.urls),
    path('account/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('home/', include(('home.urls', 'home'), namespace='home')),
    path('django_messages/', include(('django_messages.urls', 'django_messages'), namespace='django_messages')),
    path('compose/', include(('django_messages.urls', 'django_messages'), namespace='django_messages')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
