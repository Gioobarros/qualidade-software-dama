class UsuarioAdminMixin:
    def get_username(self, objeto):
        if objeto.user:
            return objeto.user.username
        return "sem username"

    def get_email(self, objeto):
        if objeto.user:
            return objeto.user.email
        return "sem email"

    def get_status(self, objeto):
        if objeto.user:
            return objeto.user.status
        return "sem status"

    # Configurar descrições dos métodos
    get_username.short_description = "Usuário"
    get_email.short_description = "E-mail"
    get_status.short_description = "Status"
