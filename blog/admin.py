from django.contrib import admin
from .models import Post, Galeria

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha')
    search_fields = ('titulo',)
    date_hierarchy = 'fecha'


@admin.register(Galeria)
class GaleriaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'activo')
    list_editable = ('activo',)