from django.urls import path
from .views import marketplace, anunciar

urlpatterns = [
    path('', marketplace, name='marketplace'),
    path('anunciar', anunciar, name='anunciar'),
]
