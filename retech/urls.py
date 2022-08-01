from django.contrib import admin
from django.urls import path, include
from home.views import home
from information.views import information

urlpatterns = [
    path('admin/', admin.site.urls),

    # HOME
    path('', home, name='home'),

    # INFORMATION
    path('information/', information, name='information'),

]
