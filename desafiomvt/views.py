from multiprocessing import context
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from familia.models import Familiares

def create_fam(request):
    agus = Familiares.objects.create(name = 'Agustina', lastname = "Garrocho", fechaNacimiento = '1992-03-05', edad = 30)

    
    context = {
        'agus': agus
    }
    return render(request, 'create_familia.html', context=context )
    
def list_fam(request):
    familiares = Familiares.objects.all()
    context = {
        'familiares': familiares
    }
    return render(request, 'familia.html', context=context)