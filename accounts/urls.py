from django.urls import path
from . import views

urlpatterns = [
    path('register/fisica', views.signUp_pf, name='signup_pf'),
    path('register/pj', views.signUp_pj, name='signup_pj'),
    path('profile/', views.profile, name='profile'),
]