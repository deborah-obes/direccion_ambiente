# blog/forms.py
from django import forms
from .models import Galeria, Publicacion

class GaleriaForm(forms.ModelForm):
    class Meta:
        model = Galeria
        fields = ['titulo', 'url', 'album_url', 'imagen', 'descripcion', 'activo']
        widgets = {
                'album_url': forms.URLInput(attrs={'placeholder': 'https://photos.app.goo.gl/... (nuevo)'})
        }

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'resumen', 'memoria', 'foto']