from django.shortcuts import render
from django.http import HttpResponse
from .models import Locacao, Filme


# Create your views here.
def index(request):
    context = {'mensagem': "Aqui você vai encontrar uma locadora de filmes. Vitória Naomí Martins Reis"}
    return render(request, 'locadora/index.html', context)

def lista_locacao(request):
    locacoes = Locacao.objects.all()
    context = {'locacoes': locacoes}
    return render(request, 'locadora/locacao.html', context)

def lista_filmes(request):
    filmes = Filme.objects.all()
    context = {'filmes': filmes}
    return render(request, 'locadora/filme.html', context)
