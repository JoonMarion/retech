from django.shortcuts import render
from utils import *
from .models import Company
from django.core.paginator import Paginator

# Create your views here.
def service(request):
    data = {}
    search = request.GET.get('search')
    if search:
        model = Company.objects.filter(address__city__icontains=search) | Company.objects.filter(address__state__icontains=search)
    else:
        model = Company.objects.all()
    for obj in model:
        obj.phone = phone_formatted(obj.phone)
    paginator = Paginator(model, 3)
    page = request.GET.get('page')
    data['db'] = paginator.get_page(page)
    return render(request, 'service.html', data)

def search_address_company(request):

    return render(request, 'search_address_company.html')