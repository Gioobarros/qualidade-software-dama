from django.urls import path
from api.view.administrador import AdministradorView
from api.view.profissional import ProfissionalView
from api.view.relato import RelatoView
from api.view.ong import OngView
from api.view.usuario import UsuarioView
from api.view.auth import LoginView, LogoutView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'relato', RelatoView, basename='relato')
router.register(r'ong', OngView, basename='ong')
router.register(r'profissional', ProfissionalView, basename='profissional')
router.register(r'admin', AdministradorView, basename='admin')
router.register(r'usuario', UsuarioView, basename='usuario')
router.register(r'login', LoginView, basename='login')
router.register(r'logout', LogoutView, basename='logout')

# http://127.0.0.1:8000/api/relato/?data_inicio=(yyyy-mm-dd)&data_fim=(yyyy-mm-dd)&palavra_chave=&status
