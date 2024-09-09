from django.http import HttpResponse
from django.shortcuts import render  # ler um arquivo e renderizar


def home(request):
    #return HttpResponse('Home new')
    return render(request,'recipes/home.html',status=201, context={
        'nome' : 'Estudos Django'
    })


