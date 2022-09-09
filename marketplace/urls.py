from django.urls import path
from .views import marketplace, anunciar, descricao_produto

urlpatterns = [
    path('', marketplace, name='marketplace'),
    path('anunciar', anunciar, name='anunciar'),
    path('produto/<str:tipo>/<str:name>/<int:cod>', descricao_produto, name='descricao_produto'),
]
