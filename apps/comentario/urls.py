from django.urls import path
from .views import *

app_name = 'apps.comentario'

urlpatterns = [
    path('comentar/<int:id>/', ComentarArticuloView.as_view(), name='comentarArticulo'),
    path('listComentario/', ListadoComentarioView.as_view(), name='listComentario'),
    path('addComentario/', AgregarComentarioView.as_view(), name='addComentario'),
    path('eliminarComentario/<int:pk>/', DeleteComentario.as_view(), name='eliminarComentario'),
    path('detalleArticulo/<int:articulo_id>/', DetalleArticuloView.as_view(), name='detalleArticulo'),

     # 👉 ESTA ES LA QUE USA eliminarComentario.js
    path('eliminarComentario/<int:pk>/', DeleteComentario.as_view(), name='eliminarComentario'),

    # Editar Cometario
    path('<int:pk>/editar/', ComentarioUpdateView.as_view(), name='editarComentario'),
]
