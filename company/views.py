from django.shortcuts import render
from utils import *
from .models import Company

# Create your views here.
def service(request):
    model = Company.objects.all()
    for obj in model:
        obj.phone = phone_formatted(obj.phone)
    return render(request, 'service.html', {'model': model})