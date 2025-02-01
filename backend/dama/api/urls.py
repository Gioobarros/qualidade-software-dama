from django.urls import path
from api.view.administrador import AdministradorView
from api.view.profissional import ProfissionalView
from api.view.relato import RelatoView, AlterarRelatoView
from api.view.ong import OngView
from api.view.auth import LoginView, LogoutView

urlpatterns = [
    path('ong/', OngView.as_view(), name='ong'),
    path('profissional/', ProfissionalView.as_view(), name='profissional'),
    path('relato/', RelatoView.as_view(), name='criar_relato'),
    path('relato/<uuid:id>', AlterarRelatoView.as_view(), name='alterar_relato'),
    path('administrador/', AdministradorView.as_view(), name='administrador'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]