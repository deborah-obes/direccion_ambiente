from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

app_name = 'apps.usuario'

urlpatterns = [
    path('registrar/', RegistrarUsuario.as_view(), name='registrar'),
    path('login/', LoginUsuario.as_view(), name='login'),
    path('logout/', LogoutUsuario.as_view(), name='logout'),
   
    path('password_reset/', RecuperarContraView.as_view(), name='password_reset'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    path('usuario/', UsuarioListView.as_view(), name='listUsuario'),

   # 👉 eliminarUsuario.js
    path('eliminarUsuario/<int:id>/', UsuarioDeleteView.as_view(), name='eliminarUsuario'),
   # Deshabilitar Usuario
    path('usuario/toggle/<int:id>/', UsuarioToggleActiveView.as_view(), name='toggleUsuario'),

]
