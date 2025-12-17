from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),   # ← este name='inicio' es el que usa {% url %}
    path('galeria/', views.galeria, name='galeria'),
    path('nosotros/', views.nosotros, name='nosotros'),
]