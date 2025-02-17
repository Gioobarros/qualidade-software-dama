from django.urls import path
from api.view.administrador import AdministradorView
from api.view.profissional import ProfissionalView
from api.view.relato import RelatoView
from api.view.ong import OngView
from api.view.auth import LoginView, LogoutView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'relato', RelatoView, basename='relato')

# http://127.0.0.1:8000/api/relato/?data_inicio=(yyyy-mm-dd)&data_fim=(yyyy-mm-dd)&palavra_chave=()

urlpatterns = [
    path('ong/', OngView.as_view(), name='ong'),
    path('profissional/', ProfissionalView.as_view(), name='profissional'),
    path('administrador/', AdministradorView.as_view(), name='administrador'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

urlpatterns += router.urls