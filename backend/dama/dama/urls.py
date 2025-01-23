from api.view.ong import OngView
from django.contrib import admin
from django.urls import path, include
from api.view.relato import RelatoView
from api.view.auth import LoginView, LogoutView
from rest_framework.routers import DefaultRouter
from api.view.profissional import ProfissionalView
from api.view.administrador import AdministradorView

app_name = 'api'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'))

]