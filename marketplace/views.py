from random import shuffle
from django.shortcuts import render, redirect
from .models import AnuncioVenda, AnuncioDoacao
from company.models import Address
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
            contexto = {'inputtype': 'number">'}
        
        if request.GET.get('tipoanuncio') == 'doacao':
            contexto = {'inputtype': 'hidden'}

    if request.method == 'POST':
        novo_endereco = Address(
            city=request.POST['cidade'].capitalize(),
            state=request.POST['estado'].upper(),
        )
        novo_endereco.save()
        if request.POST['tipoanuncio'] == 'venda':
            novo_anuncio = AnuncioVenda(
                title=request.POST['titulo'],
                description=request.POST['descricao'],
                price=request.POST['preco'],
                address=novo_endereco,
                user=request.user,
            )
            novo_anuncio.save()
            return redirect('/marketplace')




    return render(request, 'anunciar.html', {'contexto': contexto})
