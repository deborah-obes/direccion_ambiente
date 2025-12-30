# blog/views.py
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import views as auth_views
from django.contrib import messages
from django.http import Http404
from django.core.paginator import Paginator
from .models import Post, Galeria, Publicacion
from .forms import GaleriaForm, PublicacionForm


# --------------------  AUX  --------------------
def es_super(user):
    return user.is_superuser


# --------------------  VISTAS PÚBLICAS  --------------------
def inicio(request):
    publicaciones = Publicacion.objects.all()[:6]
    return render(request, 'blog/inicio.html', {
        'publicaciones': publicaciones,
        'titulo_sitio': 'Misiones y funciones'
    })


def galeria(request):
    paginator = Paginator(Galeria.objects.filter(activo=True).order_by('titulo'), 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/galeria.html', {
        'page_obj': page_obj,
        'titulo_sitio': 'Dirección de Ambiente y Espacios Verdes'
    })


def nosotros(request):
    equipo = request.session.get('equipo', [
        {"nombre": "Arq. Filippis, Ivana", "rol": "Directora de Proyectos"},
        {"nombre": "Coppola, David", "rol": "Jefe Dto. de Proyectos"},
        {"nombre": "Arq. Aguirre, Fernando", "rol": "Dibujante Proyectista"},
        {"nombre": "Arq. Cáceres, Gabriel", "rol": "Dibujante Proyectista"},
        {"nombre": "Ing. Medina, Mariela", "rol": "Calculista Estructural"},
        {"nombre": "Arq. Obes, Déborah", "rol": "Dibujante Proyectista"},
    ])
    request.session['equipo'] = equipo
    return render(request, 'blog/nosotros.html', {
        'equipo': equipo,
        'titulo_sitio': 'Dirección de Ambiente y Espacios Verdes'
    })


# --------------------  ABM GALERÍA  --------------------
@user_passes_test(es_super)
def galeria_agregar(request):
    page = request.POST.get('page') or request.GET.get('page')
    if request.method == 'POST':
        form = GaleriaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            url = reverse('blog:galeria')
            if page:
                url += f'?page={page}'
            return redirect(url)
    else:
        form = GaleriaForm()
    return render(request, 'blog/galeria_form.html', {
        'form': form,
        'page': page,
        'titulo_sitio': 'Dirección de Ambiente y Espacios Verdes'
    })


@user_passes_test(es_super)
def galeria_editar(request, pk):
    item = get_object_or_404(Galeria, pk=pk)
    page = request.POST.get('page') or request.GET.get('page')
    if request.method == 'POST':
        form = GaleriaForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            url = reverse('blog:galeria')
            if page:
                url += f'?page={page}'
            return redirect(url)
    else:
        form = GaleriaForm(instance=item)
    return render(request, 'blog/galeria_form.html', {
        'form': form,
        'page': page,
        'titulo_sitio': 'Dirección de Ambiente y Espacios Verdes'
    })


@user_passes_test(es_super)
def galeria_eliminar(request, pk):
    item = get_object_or_404(Galeria, pk=pk)
    page = request.POST.get('page') or request.GET.get('page')
    if request.method == 'POST':
        item.delete()
        url = reverse('blog:galeria')
        if page:
            url += f'?page={page}'
        return redirect(url)
    return render(request, 'blog/galeria_confirmar_borrar.html', {
        'item': item,
        'page': page,
        'titulo_sitio': 'Dirección de Ambiente y Espacios Verdes'
    })


# --------------------  ABM PUBLICACIONES  --------------------
@user_passes_test(lambda u: u.is_superuser)
def lista_publicaciones(request):
    paginator = Paginator(Publicacion.objects.all().order_by('-fecha_hora'), 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/lista_publicaciones.html', {
        'page_obj': page_obj,
        'titulo_sitio': 'Dirección de Ambiente y Espacios Verdes'
    })


def pub_detalle(request, pk):
    pub = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'blog/pub_detalle.html', {
        'pub': pub,
        'titulo_sitio': 'Dirección de Ambiente y Espacios Verdes'
    })


@user_passes_test(lambda u: u.is_superuser)
def pub_crear(request):
    page = request.POST.get('page') or request.GET.get('page')
    if request.method == 'POST':
        form = PublicacionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            url = reverse('blog:lista_publicaciones')
            if page:
                url += f'?page={page}'
            return redirect(url)
    else:
        form = PublicacionForm()
    return render(request, 'blog/pub_form.html', {
        'form': form,
        'page': page,
        'titulo_sitio': 'Dirección de Ambiente y Espacios Verdes'
    })


@user_passes_test(lambda u: u.is_superuser)
def pub_editar(request, pk):
    pub = get_object_or_404(Publicacion, pk=pk)
    page = request.POST.get('page') or request.GET.get('page')
    if request.method == 'POST':
        form = PublicacionForm(request.POST, request.FILES, instance=pub)
        if form.is_valid():
            form.save()
            url = reverse('blog:lista_publicaciones')
            if page:
                url += f'?page={page}'
            return redirect(url)
    else:
        form = PublicacionForm(instance=pub)
    return render(request, 'blog/pub_form.html', {
        'form': form,
        'page': page,
        'titulo_sitio': 'Dirección de Ambiente y Espacios Verdes'
    })


@user_passes_test(lambda u: u.is_superuser)
def pub_borrar(request, pk):
    pub = get_object_or_404(Publicacion, pk=pk)
    page = request.POST.get('page') or request.GET.get('page')
    if request.method == 'POST':
        pub.delete()
        url = reverse('blog:lista_publicaciones')
        if page:
            url += f'?page={page}'
        return redirect(url)
    return render(request, 'blog/pub_confirmar_borrar.html', {
        'pub': pub,
        'page': page,
        'titulo_sitio': 'Dirección de Ambiente y Espacios Verdes'
    })


# --------------------  ABM MIEMBROS  --------------------
@user_passes_test(es_super)
def editar_miembro(request, id):
    equipo = request.session.get('equipo', [])
    if id < 0 or id >= len(equipo):
        raise Http404("Miembro no encontrado")
    miembro = equipo[id]
    if request.method == 'POST':
        miembro['nombre'] = request.POST.get('nombre')
        miembro['rol'] = request.POST.get('rol')
        request.session['equipo'] = equipo
        messages.success(request, 'Miembro actualizado.')
        return redirect('blog:nosotros')
    return render(request, 'blog/editar_miembro.html', {
        'miembro': miembro,
        'id': id,
        'titulo_sitio': 'Dirección de Ambiente y Espacios Verdes'
    })


@user_passes_test(es_super)
def eliminar_miembro(request, id):
    equipo = request.session.get('equipo', [])
    if id < 0 or id >= len(equipo):
        raise Http404("Miembro no encontrado")
    miembro = equipo[id]
    if request.method == 'POST':
        equipo.pop(id)
        request.session['equipo'] = equipo
        messages.success(request, 'Integrante eliminado.')
        return redirect('blog:nosotros')
    return render(request, 'blog/confirmar_eliminar.html', {
        'miembro': miembro,
        'titulo_sitio': 'Dirección de Ambiente y Espacios Verdes'
    })


@user_passes_test(es_super)
def agregar_miembro(request):
    equipo = request.session.get('equipo', [])
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        rol = request.POST.get('rol')
        if nombre and rol:
            equipo.append({'nombre': nombre, 'rol': rol})
            request.session['equipo'] = equipo
            messages.success(request, 'Integrante agregado.')
            return redirect('blog:nosotros')
    return render(request, 'blog/agregar_miembro.html', {
        'titulo_sitio': 'Dirección de Ambiente y Espacios Verdes'
    })