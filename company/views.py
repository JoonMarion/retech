from django.shortcuts import render
from .models import Company

# Create your views here.
def service(request):
    model = Company.objects.all()
    return render(request, 'service.html', {'model': model})