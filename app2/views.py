from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1>soy el index de la segunda app</h1>")

def respuesta(request):
    return HttpResponse("<h2>funcionando desde la app2</h2>")