from django.shortcuts import render, redirect
from django.urls import reverse_lazy


def SignUp(request):
    return render(request, 'registration/register.html')