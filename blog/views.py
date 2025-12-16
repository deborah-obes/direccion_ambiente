from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Post, Galeria

def inicio(request):
    posts = Post.objects.all().order_by('-fecha')
    return render(request, 'blog/inicio.html', {
        'posts': posts,
        'titulo_sitio': 'Dirección de Ambiente y Espacios Verdes'
    })

@login_required
def galeria(request):
    galeria = Galeria.objects.filter(activo=True).first()
    return render(request, 'blog/galeria.html', {
        'galeria': galeria,
        'titulo_sitio': 'Dirección de Ambiente y Espacios Verdes'
    })
