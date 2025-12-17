from .models import Usuario
from .forms import RegistroUsuarioForm
from ..articulo.models import Articulo
from ..comentario.models import Comentario
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.auth.models import Group
from django.views.generic import CreateView, ListView, DeleteView
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.contrib.auth.models import User
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import get_user_model

class RegistrarUsuario(CreateView):
    template_name = 'registracion/registrar.html'
    form_class = RegistroUsuarioForm

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Registro exitoso. Por favor, inicia sesión.')
        group = Group.objects.get(name='registrado')
        self.object.groups.add(group)
        return redirect('apps.usuario:login')

class LoginUsuario(LoginView):
    template_name = 'registracion/login.html'

    def get_success_url(self):
        messages.success(self.request, 'Login exitoso')
        return reverse('index')
     
class LogoutUsuario(LogoutView):
    next_page = 'index'
    template_name = 'registracion/logout.html'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.success(request, 'Logout exitoso')
        return response

class UsuarioListView(LoginRequiredMixin, ListView):
    model = Usuario
    template_name = 'usuario/listUsuario.html'
    context_object_name = 'usuarios'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.exclude(is_superuser=True)
        return queryset

class UsuarioDeleteView(LoginRequiredMixin, DeleteView):
    model = Usuario
    template_name = 'apps.usuario:listUsuario'
    success_url = reverse_lazy('apps.usuario:listUsuario')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        colaborador_group = Group.objects.get(name='Colaborador')
        es_colaborador = colaborador_group in self.object.groups.all()
        context['es_colaborador'] = es_colaborador
        return context

    def post(self, request, *args, **kwargs):
        eliminar_comentarios = request.POST.get('eliminarComentarios', False)
        eliminar_posts = request.POST.get('eliminarPosts', False)
        self.object = self.get_object()
        if eliminar_comentarios:
            Comentario.objects.filter(usuario=self.object).delete()

        if eliminar_posts:
            Articulo.objects.filter(autor=self.object).delete()
        messages.success(request, f'Usuario {self.object.username} eliminado correctamente')
        return self.delete(request, *args, **kwargs)
    
#RecuperarContra
class RecuperarContraView(PasswordResetView):
    template_name = 'registracion/recuperarContra.html'

    def get_success_url(self):
        messages.success(self.request, 'Se envió un email de recuperación. Revise su casilla de correo para recuperar su cuenta.')
        return reverse('index')
    
#Deshabilitar Usuario
User = get_user_model()

class UsuarioToggleActiveView(LoginRequiredMixin, UserPassesTestMixin, View):

    def test_func(self):
        # Solo admins o colaboradores pueden hacerlo
        return self.request.user.is_superuser or self.request.user.groups.filter(name='Colaborador').exists()

    def post(self, request, id):
        usuario = get_object_or_404(User, id=id)

        usuario.is_active = not usuario.is_active
        usuario.save()

        estado = "habilitado" if usuario.is_active else "deshabilitado"
        messages.success(request, f"El usuario {usuario.username} fue {estado} correctamente.")

        return redirect("apps.usuario:listUsuario")