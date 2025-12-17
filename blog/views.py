from django.shortcuts import render
from .models import Post, Galeria

def inicio(request):
    posts = Post.objects.all().order_by('-fecha')
    return render(request, 'blog/inicio.html', {
        'posts': posts,
        'titulo_sitio': 'Dirección de Ambiente y Espacios Verdes'
    })

def galeria(request):
    galeria = Galeria.objects.filter(activo=True).first()
    return render(request, 'blog/galeria.html', {
        'galeria': galeria,
        'titulo_sitio': 'Dirección de Ambiente y Espacios Verdes'
    })

def nosotros(request):
    equipo = [
        {"nombre": "Juan Pérez", "rol": "Director de Proyectos"},
        {"nombre": "María Gómez", "rol": "Coordinadora Ambiental"},
    ]
    return render(request, 'blog/nosotros.html', {
        'equipo': equipo,
        'titulo_sitio': 'Dirección de Ambiente y Espacios Verdes'
    })