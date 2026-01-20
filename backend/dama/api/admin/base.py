from api.constants import MESSAGES


class UsuarioAdminMixin:
    """Mixin para adicionar campos de usuário aos admins de modelos."""

    def get_username(self, objeto):
        """Retorna o username do usuário associado ao objeto."""
        if objeto.user:
            return objeto.user.username
        return "sem username"

    def get_email(self, objeto):
        """Retorna o email do usuário associado ao objeto."""
        if objeto.user:
            return objeto.user.email
        return "sem email"

    def get_status(self, objeto):
        """Retorna o status do usuário associado ao objeto."""
        if objeto.user:
            return objeto.user.status
        return "sem status"

    # Configurar descrições dos métodos
    get_username.short_description = "Usuário"
    get_email.short_description = "E-mail"
    get_status.short_description = "Status"
