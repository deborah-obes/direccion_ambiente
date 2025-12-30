# blog/models.py
from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'

    def __str__(self):
        return self.titulo


class Galeria(models.Model):
    titulo = models.CharField(max_length=120, verbose_name='Nombre del álbum')
    url = models.URLField(help_text='Enlace público de Google Fotos')   # viejo
    album_url = models.URLField('Enlace a álbum Google Photos', blank=True)  # nuevo
    imagen = models.ImageField(upload_to='galeria/', blank=True, verbose_name='Imagen de portada')
    descripcion = models.TextField(blank=True, verbose_name='Descripción')
    activo = models.BooleanField(default=True, verbose_name='Mostrar')

    class Meta:
        verbose_name_plural = 'Galerías'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo


class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    resumen = models.TextField(max_length=300)
    memoria = models.TextField()
    foto = models.ImageField(upload_to='pub_fotos/')
    fecha_hora = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_hora']
        verbose_name_plural = 'Publicaciones'

    def __str__(self):
        return self.titulo
    