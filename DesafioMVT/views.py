from django.shortcuts import render
from django.http import HttpResponse
from DesafioMVT.models import Familiar

# Create your views here.
def home(request):
    
    return render(request, "AppCoder/home.html")

def familiar(self):
    f1 = Familiar(nombre = "Paula", apellido = "Garrocho", relacion = "Yo", fechaNac = "1994-02-25")
    f1.save()

    f2 = Familiar(nombre = "Agustina", apellido = "Garrocho", relacion = "Hermana", fechaNac = "1992-03-05")                              
    f2.save()

    f3 = Familiar(nombre = "Elena", apellido = "Dowling", relacion = "Madre", fechaNac = "1952-12-22")
    f3.save()
    
    f4 = Familiar(nombre = "Marcos", apellido = "Lescano", relacion = "Novio", fechaNac = "1991-11-10")
    f4.save()

    pau = f"Mi nombre es: {f1.nombre}, Apellido: {f1.apellido}, Relación: {f1.relacion}, fecha de nacimiento: {f1.fechaNac}" 
    agus = f"<br> Mi hermana es: {f2.nombre}, Apellido: {f2.apellido}, Relación: {f2.relacion}, fecha de nacimiento: {f2.fechaNac}"
    ma = f"<br> Mi mamá es: {f3.nombre}, Apellido: {f3.apellido}, Relación: {f3.relacion}, fecha de nacimiento: {f3.fechaNac}"
    mar = f"<br> Mi novio es: {f4.nombre}, Apellido: {f4.apellido}, Relación: {f4.relacion}, fecha de nacimiento: {f4.fechaNac}"
    familia = pau + agus + ma + mar
    return HttpResponse(familia)