from .models import Articulo,  Categoria
from apps.comentario.models import Comentario
from .forms import ArticuloForm, NuevaCategoriaForm
from apps.comentario.forms import ComentarioForm
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.contrib import messages

#Todos los artículos
class ArticuloListView(ListView):
    model = Articulo
    template_name = "articulo/articulos.html" 
    context_object_name = "articulos" 

    def get_queryset(self):
        queryset = super().get_queryset()
        orden = self.request.GET.get('orden')
        if orden == 'reciente':
            queryset = queryset.order_by('-fecha_publicacion')
        elif orden == 'antiguo':
            queryset = queryset.order_by('fecha_publicacion')
        elif orden == 'alfabetico':
            queryset = queryset.order_by('titulo')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orden'] = self.request.GET.get('orden', 'reciente')
        return context


def post(self, request, *args, **kwargs):

    # Detectar si se está editando
    edit_id = request.GET.get("edit")
    if edit_id:
        comentario = Comentario.objects.get(pk=edit_id)
        form = ComentarioForm(request.POST, instance=comentario)

        if form.is_valid():
            form.save()
            messages.success(request, "Comentario actualizado con éxito.")
            return redirect('apps.articulo:articuloDetalle', id=self.kwargs['id'])

    # Si NO es edición → crear comentario nuevo
    form = ComentarioForm(request.POST)
    if form.is_valid():
        comentario = form.save(commit=False)
        comentario.usuario = request.user
        comentario.articulo_id = self.kwargs['id']
        comentario.save()
        messages.success(self.request, 'Comentario creado con éxito.')
        return redirect('apps.articulo:articuloDetalle', id=self.kwargs['id'])

    # Si hay errores
    context = self.get_context_data(**kwargs)
    context['form'] = form
    return self.render_to_response(context)


# Artículo individual
class ArticuloDetailView(DetailView):
    model = Articulo
    template_name = "articulo/postArticulos.html"
    success_url = 'articulo'
    context_object_name = "articulo"
    pk_url_kwarg = "id"
    queryset = Articulo.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Comentarios del artículo
        context['comentarios'] = Comentario.objects.filter(articulo_id=self.kwargs['id'])

        # ¿Editar comentario?
        edit_id = self.request.GET.get("edit")
        if edit_id:
            comentario = Comentario.objects.get(pk=edit_id)
            context['editando'] = True
            context['comentario_editar'] = comentario
            context['form'] = ComentarioForm(instance=comentario)
        else:
            context['editando'] = False
            context['form'] = ComentarioForm()

        return context

    def post(self, request, *args, **kwargs):
        """Crear comentario nuevo."""
        form = ComentarioForm(request.POST)
        if form.is_valid():
            messages.success(self.request, 'Comentario creado con éxito.')
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.articulo_id = self.kwargs['id']
            comentario.save()
            return redirect('apps.articulo:articuloDetalle', id=self.kwargs['id'])
        
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)



#Artículo creación
class ArticuloCreateView(LoginRequiredMixin, CreateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'articulo/articulo_form.html'

    def get_success_url(self):
            messages.success(self.request, '¡Artículo creado con éxito!')
            return reverse_lazy('apps.articulo:articulos')


#Artículo modificación
class ArticuloUpdateView(LoginRequiredMixin, UpdateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'articulo/articulo_form.html'

    def get_success_url(self):
            messages.success(self.request, '¡Artículo modificado con éxito!')
            return reverse_lazy('apps.articulo:articulos')


#Articulo borrar
class ArticuloDeleteView(DeleteView):
    model = Articulo
    #template_name = 'articulo/eliminarArticulo.html' voy a utilizar sweet alert

    def get_success_url(self):
        messages.success(self.request, '¡Borrado con éxito!')
        return reverse_lazy('apps.articulo:articulos')
    

class ArticuloPorCategoriaView(ListView):
    model = Articulo
    template_name = 'articulo/articulosPorCategoria.html'
    context_object_name = 'articulos'

    def get_queryset(self):
        return Articulo.objects.filter(categoria_id=self.kwargs['pk'])
    
#Categorías
class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    form_class = NuevaCategoriaForm
    template_name = 'articulo/crearCategoria.html'

    def get_success_url(self):
        messages.success(self.request, '¡Categoría creada con éxito!')
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        else:
            return reverse_lazy('apps.articulo:crearArticulo')

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'articulo/listCategoria.html'
    context_object_name = 'categorias'

class CategoriaDeleteView(DeleteView):
    model = Categoria
    #template_name = 'articulo/eliminarCategoria.html'
    success_url = reverse_lazy('apps.articulo:listCategoria')
