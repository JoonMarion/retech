from random import shuffle
from django.shortcuts import render, redirect
from .models import AnuncioVenda, AnuncioDoacao
from company.models import Address
from .models import AnuncioVenda, AnuncioDoacao
from accounts.models import Perfil


# Create your views here.
def marketplace(request):
    produtos = list(AnuncioVenda.objects.filter(estado="A")) + list(AnuncioDoacao.objects.filter(estado="A"))
    shuffle(produtos)
    return render(request, 'marketplace.html', {'produtos': produtos})


def anunciar(request):
    usuario = Perfil.objects.get(user=request.user)
    contexto = {}
    if request.method == 'GET':
        if request.GET.get('tipoanuncio') == 'venda':
            contexto = {'inputtype': 'number">'}
        
        if request.GET.get('tipoanuncio') == 'doacao':
            contexto = {'inputtype': 'hidden'}

    if request.method == 'POST':
        if request.POST.get('tipoanuncio') == 'venda':
            novo_anuncio = AnuncioVenda.objects.create(
                nome_prod=request.POST['titulo'],
                descricao_prod=request.POST['descricao'],
                categoria=request.POST['categoria'],
                preco_prod=request.POST['preco'],
                cidade=request.POST['cidade'],
                user=request.user,
            )

        if request.POST.get('tipoanuncio') == 'doacao':
            novo_anuncio = AnuncioDoacao.objects.create(
                nome_prod=request.POST['titulo'],
                descricao_prod=request.POST['descricao'],
                categoria=request.POST['categoria'],
                cidade=request.POST['cidade'],
                user=request.user,
            )



    return render(request, 'anunciar.html', {'contexto': contexto, 'usuario': usuario})