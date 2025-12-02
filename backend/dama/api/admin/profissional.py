from django.contrib import admin
from api.models.profissional import Profissional
from .base import UsuarioAdminMixin


@admin.register(Profissional)
class AdminProfissional(UsuarioAdminMixin, admin.ModelAdmin):
    list_display = ("id", "nome_completo", "conselho", "get_username", "get_email", "bio")
    search_fields = ("user__username", "nome_completo", "conselho", "user__status")
