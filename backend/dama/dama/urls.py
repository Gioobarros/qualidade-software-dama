from api.view.ong import OngView
from django.contrib import admin
from django.urls import path, include
from api.view.relato import RelatoView
from api.view.auth import LoginView, LogoutView
from rest_framework.routers import DefaultRouter
from api.view.profissional import ProfissionalView
from api.view.administrador import AdministradorView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/ong/', OngView.as_view(), name='ong'),
    path('api/profissional/', ProfissionalView.as_view(), name='profissional'),
    path('api/relato/', RelatoView.as_view(), name='relato'),
    path('api/administrador/', AdministradorView.as_view(), name='administrador'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
]