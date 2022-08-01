from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home.views import home
from information.views import information
from company.views import search

urlpatterns = [
    path('admin/', admin.site.urls),

    # HOME
    path('', home, name='home'),

    # INFORMATION
    path('information/', information, name='information'),

    # SEARCH
    path('search/', search, name='search'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
