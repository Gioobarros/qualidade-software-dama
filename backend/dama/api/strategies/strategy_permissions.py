from abc import ABC, abstractmethod
from rest_framework.permissions import IsAuthenticated, AllowAny

class PermissaoStrategy(ABC):
    @abstractmethod
    def get_permissions(self, action):
        pass

class UsuarioPermission(PermissaoStrategy):
    def get_permissions(self, action):
        if action in ['partial_update', 'destroy']:
            return [IsAuthenticated()]
        return [AllowAny()]
    
class RelatoPermission(PermissaoStrategy):

    def get_permissions(self, action):
        if action in ['create', 'partial_update', 'destroy']:
            return [IsAuthenticated()]
        return [AllowAny()]
    
    def validar(self, user):
        if user.perfil == 'admin':
            raise ValueError("Perfil de publicador inválido.")



