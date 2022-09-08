from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from company.models import Address
from .models import Perfil
import uuid

def signUp(request):

    if request.method == 'POST':
        if request.POST['senha1'] == request.POST['senha2']:
            username = request.POST['nome'] + str(uuid.uuid4())
            novo_usuario = User.objects.create_user(
                username=username,
                email=request.POST['email'],
                password=request.POST['senha1'],
            )

            novo_endereco = Address.objects.create(
                street=request.POST['rua'],
                number=request.POST['numero'],
                complement=request.POST['complemento'],
                district=request.POST['bairro'],
                city=request.POST['cidade'],
                state=request.POST['estado'],
                cep=request.POST['cep'],
            )

            novo_perfil = Perfil.objects.create(
                name=request.POST['nome'],
                lastname=request.POST['sobrenome'],
                birth_date=request.POST['data'],
                user=novo_usuario,
                address=novo_endereco,
            )

            return redirect('/accounts/login')


    return render(request, 'registration/register.html')

def profile(request):
    print(request.user)

    print(Perfil.objects.get(user=request.user).name)
    return render(request, 'registration/profile.html', {'perfil': Perfil.objects.get(user=request.user)})