from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home.views import home
from information.views import information
from company.views import service

urlpatterns = [
    path('admin/', admin.site.urls),

    # HOME
    path('/', home, name='home'),

    # INFORMATION
    path('information/', information, name='information'),

    # service
    path('service/', service, name='service'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
