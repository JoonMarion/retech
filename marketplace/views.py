from random import shuffle
from django.shortcuts import render, redirect
from .models import AnuncioVenda, AnuncioDoacao


# Create your views here.
def marketplace(request):
    produtos = list(AnuncioVenda.objects.filter(estado="A")) + list(AnuncioDoacao.objects.filter(estado="A"))
    shuffle(produtos)
    return render(request, 'marketplace.html', {'produtos': produtos})


def anunciar(request):
    contexto = {}
    if request.method == 'GET':
        if request.GET.get('tipoanuncio') == 'venda':
            contexto = {'form': 'number">'}
        
        if request.GET.get('tipoanuncio') == 'doacao':
            contexto = {'form': 'hidden'}

    if request.method == 'POST':
        pass
    return render(request, 'anunciar.html', {'contexto': contexto})
