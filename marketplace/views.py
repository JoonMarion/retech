from random import shuffle
from django.shortcuts import render, redirect, get_object_or_404
from .models import AnuncioVenda, AnuncioDoacao
from company.models import Address
from .models import AnuncioVenda, AnuncioDoacao
from accounts.models import Perfil
from django.core.files.storage import FileSystemStorage
import uuid


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
            contexto = {'inputtype': 'number'}
        
        if request.GET.get('tipoanuncio') == 'doacao':
            contexto = {'inputtype': 'hidden'}

    if request.method == 'POST':
        tipoanuncio = request.POST.get('tipoanuncio')
        print(tipoanuncio)
        if tipoanuncio == 'venda':
            novo_anuncio = AnuncioVenda.objects.create(
                nome_prod=request.POST.get('titulo'),
                categoria=request.POST.get('categoria'),
                descricao_prod=request.POST.get('descricao'),
                preco_prod=request.POST.get('preco'),
                estado="A",
                user=request.user,
                img_prod=request.FILES.get('image'),
                cidade=request.POST.get('cidade')
            )
            return redirect('marketplace')
        
        if tipoanuncio == 'doacao':
            novo_anuncio = AnuncioDoacao.objects.create(
                nome_prod=request.POST.get('titulo'),
                categoria=request.POST.get('categoria'),
                descricao_prod=request.POST.get('descricao'),
                estado="A",
                user=request.user,
                img_prod=request.FILES.get('image'),
                cidade=request.POST.get('cidade')
            )

            return redirect('marketplace')


    return render(request, 'anunciar.html', {'contexto': contexto, 'usuario': usuario})


def descricao_produto(request, tipo, name, cod):
    usuario = None
    produto = None
    if tipo == 'venda':
        produto = AnuncioVenda.objects.get(pk=cod)
        usuario = Perfil.objects.get(user=produto.user)
        produto = produto
    if tipo == 'doacao':
        produto = AnuncioDoacao.objects.get(pk=cod)
        usuario = Perfil.objects.get(user=produto.user)
        produto = produto
    
    return render (request, 'produto.html', {'produto': produto, 'usuario': usuario} )
