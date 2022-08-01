from django.shortcuts import render
from .models import Company

# Create your views here.
def search(request):
    model = Company.objects.all()
    return render(request, 'search.html', {'model': model})