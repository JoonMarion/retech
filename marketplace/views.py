from random import shuffle
from django.shortcuts import render
from .models import AnuncioVenda, AnuncioDoacao


# Create your views here.
def marketplace(request):
    produtos = list(AnuncioVenda.objects.all()) + list(AnuncioDoacao.objects.all())
    shuffle(produtos)
    return render(request, 'marketplace.html', {'produtos': produtos})