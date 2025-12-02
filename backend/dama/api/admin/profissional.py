from django.contrib import admin
from api.models.profissional import Profissional


@admin.register(Profissional)
class AdminProfissional(admin.ModelAdmin):

    list_display = ("id", "nome_completo", "conselho", "get_username", "get_email", "bio")
    search_fields = ("user__username", "nome_completo", "conselho", "user__status")

    def get_username(self, objeto):
        if objeto.user:
            return objeto.user.username
        else:
            return "sem username"

    def get_email(self, objeto):
        if objeto.user:
            return objeto.user.email
        else:
            return "sem email"

    def get_status(self, objeto):
        if objeto.user:
            return objeto.user.status
        else:
            return "sem status"

    get_username.short_description = "Usuário"

    get_email.short_description = "E-mail"

    get_status.short_description = "Status"
