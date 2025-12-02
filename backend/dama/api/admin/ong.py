from django.contrib import admin
from api.models.ong import Ong
from .base import UsuarioAdminMixin


@admin.register(Ong)
class AdminOng(UsuarioAdminMixin, admin.ModelAdmin):
    list_display = ("id", "razao_social", "cnpj", "get_username", "get_email", "bio")
    search_fields = ("user__username", "razao_social", "cnpj", "user__status")
