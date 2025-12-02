from django.contrib import admin
from api.models.publicacao import Publicacao


@admin.register(Publicacao)
class AdminPublicacao(admin.ModelAdmin):
    list_display = ("id", "conteudo", "data_criacao", "get_username", "status")
    search_fields = ("publicador__username", "status")

    def get_username(self, objeto):
        if objeto.publicador:
            return objeto.publicador.username
        else:
            return "sem username"

    get_username.short_description = "Usuário"
