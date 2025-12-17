from django.urls import path
from .views import *

app_name = 'apps.articulo'

urlpatterns = [
    path('articulos/', ArticuloListView.as_view(), name='articulos'),
    path('articulos/<int:id>/', ArticuloDetailView.as_view(), name="articuloDetalle"),
    path('articulo/crear/', ArticuloCreateView.as_view(), name='crearArticulo'),
    path('articulos/<int:pk>/actualizar/', ArticuloUpdateView.as_view(), name='editarArticulo'),
    path('articulos/<int:pk>/eliminar/', ArticuloDeleteView.as_view(), name='eliminarArticulo'),

    path('eliminar/<int:pk>/', ArticuloDeleteView.as_view(), name='eliminarArticulo'),

    path('categoria/', CategoriaListView.as_view(), name='listCategoria'),
    path('categoria/<int:pk>/articulos/', ArticuloPorCategoriaView.as_view(), name='articulosPorCategoria'),
    path('articulo/categoria', CategoriaCreateView.as_view(), name='crearCategoria'),

    # 🔥 CORREGIDA
    path('categoria/<int:pk>/eliminar/', CategoriaDeleteView.as_view(), name='eliminarCategoria'),
]

