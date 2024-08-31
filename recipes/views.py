from django.http import HttpResponse
from django.shortcuts import render  # ler um arquivo e renderizar


def home(request):
    #return HttpResponse('Home new')
    return render(request,'recipes/home.html', context={
        'nome' : 'Wander de Castro'
    })

def contato(request):
    return HttpResponse('Contato new')


def sobre(request):
    return HttpResponse('Abaout new ')
