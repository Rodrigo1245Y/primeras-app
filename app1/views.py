from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    html="""
    <h1>soy index de la apli<h1>
    <h2>hola¡<h2>
    """
    return HttpResponse(html)

def pregunta(request):
    r1="""
    <h1 style="color:blue">como estas usuario<h1>
    <h2 style="color:Red">espero que bien<h2>
    """
    return HttpResponse(r1)
