from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.SignUp, name='signup'),
]