from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    texto  = models.TextField()
    fecha  = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'

    def __str__(self):
        return self.titulo


class Galeria(models.Model):
    titulo  = models.CharField(max_length=100, default='Dirección de Ambiente y Espacios Verdes')
    iframe  = models.TextField(help_text='Pegá el iframe completo de Google Photos')
    activo  = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Galerías'

    def __str__(self):
        return self.titulo