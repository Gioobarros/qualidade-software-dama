from abc import ABC, abstractmethod
from rest_framework.exceptions import PermissionDenied

class UsuarioStrategy(ABC):
    @abstractmethod
    def validar_usuario(self, perfil):
        pass

class AdminStrategy(UsuarioStrategy):
    def validar_usuario(self, request):
        admin = getattr(request.user, 'admin', None)
        if not admin:
            raise PermissionDenied("Usuário não é um admin") 
        return admin  

class ProfissionalStrategy(UsuarioStrategy):
    def validar_usuario(self, request):
        profissional = getattr(request.user, 'profissional', None)
        if not profissional:
            raise PermissionDenied("Usuário não é um profissional") 
        return profissional  

class OngStrategy(UsuarioStrategy):
    def validar_usuario(self, request):
        ong = getattr(request.user, 'ong', None)
        if not ong:
            raise PermissionDenied("Usuário não é uma ONG") 
        return ong  

