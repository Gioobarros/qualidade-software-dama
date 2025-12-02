from django.contrib import admin
from api.models.usuario import Usuario


@admin.register(Usuario)
class AdminUsuario(admin.ModelAdmin):
    list_display = ("id", "username", "email", "status", "perfil")
    search_fields = ("username", "status", "pefil")
