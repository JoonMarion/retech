from django.contrib import admin
from django.urls import path, include
from home.views import home

urlpatterns = [
    path('admin/', admin.site.urls),

    # HOME
    path('', home, name='home'),
]
