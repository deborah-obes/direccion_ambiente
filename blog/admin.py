# blog/admin.py
from django.contrib import admin
from .models import Post, Galeria, Publicacion

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha')
    search_fields = ('titulo',)
    date_hierarchy = 'fecha'

@admin.register(Galeria)
class GaleriaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'url', 'album_url', 'activo')
    list_editable = ('url', 'album_url', 'activo')
    search_fields = ('titulo',)
    list_filter = ('activo',)
    ordering = ('titulo',)

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser
    def has_add_permission(self, request):
        return request.user.is_superuser
    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_hora')
    search_fields = ('titulo',)
    date_hierarchy = 'fecha_hora'
    readonly_fields = ('fecha_hora',)