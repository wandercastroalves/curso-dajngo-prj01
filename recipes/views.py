from django.http import HttpResponse
from django.shortcuts import render  # ler um arquivo e renderizar


def home(request):
    #return HttpResponse('Home new')
    return render(request,'global/home.html')

def contato(request):
    return HttpResponse('Contato new')


def sobre(request):
    return HttpResponse('Abaout new ')
