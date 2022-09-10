from django.shortcuts import render
from utils import *
from .models import Company
from django.core.paginator import Paginator
from django.db.models import Q


def service(request):
    data = {}
    search = request.GET.get('search')
    if search:
        search_without_accents = remove_text_accents(search)
        model = Company.objects.filter(
            Q(address__city__icontains=search) | 
            Q(address__city__icontains=search_without_accents) | 
            Q(address__state__icontains=search)
        ).order_by('created_at')
    else:
        model = Company.objects.all().order_by('created_at')
    for obj in model:
        if obj.phone:
            obj.phone = phone_formatted(obj.phone)
    paginator = Paginator(model, 3)
    page = request.GET.get('page')
    data['db'] = paginator.get_page(page)

    return render(request, 'service.html', data)
