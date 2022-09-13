from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from company.models import Address, Company
from .models import Perfil
import uuid

def signUp_pf(request):
    tipo = 'pf'

    if request.method == 'POST':

        if request.POST['senha1'] and request.POST['senha1'] == request.POST['senha2']:
            username = request.POST['nome'].capitalize() + str(uuid.uuid4())
            novo_usuario = User.objects.create_user(
                username=username,
                email=request.POST['email'],
                password=request.POST['senha1'],
            )

            novo_endereco = Address.objects.create(
                street=request.POST['rua'].capitalize(),
                number=request.POST['numero'],
                complement=request.POST['complemento'].capitalize(),
                district=request.POST['bairro'].capitalize(),
                city=request.POST['cidade'].capitalize(),
                state=request.POST['estado'].capitalize(),
                cep=request.POST['cep'],
            )

            nova_pj = Perfil.objects.create(
                name=request.POST['nome'].capitalize(),
                lastname=request.POST['sobrenome'].capitalize(),
                birth_date=request.POST['data'],
                user=novo_usuario,
                address=novo_endereco,
            )

            return redirect('/accounts/login')


    return render(request, 'registration/register.html', {'tipo': tipo})


def signUp_pj(request):
    tipo = 'pj'
    if request.method == 'POST':
        if request.POST['senha1'] and request.POST['senha1'] == request.POST['senha2']:
            username = request.POST['nome'].capitalize() + str(uuid.uuid4())
            novo_usuario = User.objects.create_user(
                username=username,
                email=request.POST['email'],
                password=request.POST['senha1'],
            )

            novo_endereco = Address.objects.create(
                street=request.POST['rua'].capitalize(),
                number=request.POST['numero'],
                complement=request.POST['complemento'].capitalize(),
                district=request.POST['bairro'].capitalize(),
                city=request.POST['cidade'].capitalize(),
                state=request.POST['estado'].capitalize(),
                cep=request.POST['cep'],
            )

            nova_empresa = Company.objects.create(
                name=request.POST['nome'].capitalize(),
                description=request.POST['descricao'].capitalize(),
                cnpj=request.POST['cnpj'],
                logo=request.FILES.get('logo'),
                user=novo_usuario,
                address=novo_endereco,
                phone=request.POST['telefone'],
            )

            return redirect('/accounts/login')


    return render(request, 'registration/register.html', {'tipo': tipo})

def profile(request):
    perfil = Perfil.objects.get(user=request.user)
    return render(request, 'registration/profile.html', {'perfil': perfil})