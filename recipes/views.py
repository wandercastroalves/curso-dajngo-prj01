from django.http import HttpResponse

#from django.shortcuts import render


def home(request):
    return HttpResponse('Home new')

def contato(request):
    return HttpResponse('Contato new')


def sobre(request):
    return HttpResponse('Abaout new ')
