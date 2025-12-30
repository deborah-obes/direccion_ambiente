# blog/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'blog'

urlpatterns = [
    # Inicio
    path('', views.inicio, name='inicio'),

    # Galería
    path('galeria/', views.galeria, name='galeria'),
    path('galeria/agregar/', views.galeria_agregar, name='galeria_agregar'),
    path('galeria/editar/<int:pk>/', views.galeria_editar, name='galeria_editar'),
    path('galeria/eliminar/<int:pk>/', views.galeria_eliminar, name='galeria_eliminar'),

    # Nosotros
    path('nosotros/', views.nosotros, name='nosotros'),

    # Publicaciones
    path('publicaciones/', views.lista_publicaciones, name='lista_publicaciones'),
    path('publicaciones/nueva/', views.pub_crear, name='pub_crear'),
    path('publicaciones/<int:pk>/', views.pub_detalle, name='pub_detalle'),
    path('publicaciones/<int:pk>/editar/', views.pub_editar, name='pub_editar'),
    path('publicaciones/<int:pk>/borrar/', views.pub_borrar, name='pub_borrar'),

    # Miembros del equipo
    path('miembros/agregar/', views.agregar_miembro, name='agregar_miembro'),
    path('miembros/<int:id>/editar/', views.editar_miembro, name='editar_miembro'),
    path('miembros/<int:id>/eliminar/', views.eliminar_miembro, name='eliminar_miembro'),

    # Login / Logout
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
]