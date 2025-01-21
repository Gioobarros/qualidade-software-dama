from django.contrib import admin
from api.view.ong import OngViewSet
from django.urls import path, include
from api.view.relato import RelatoViewSet
from rest_framework.routers import DefaultRouter
from api.view.profissional import ProfissionalViewSet
from api.view.administrador import AdministradorViewSet 
from api.view.auth import LoginViewSet, LogoutViewSet 

router = DefaultRouter()
router.register(r'profissional', ProfissionalViewSet)
router.register(r'ong', OngViewSet)
router.register(r'relato', RelatoViewSet)
router.register(r'administrador', AdministradorViewSet)
router.register(r'login', LoginViewSet)
router.register(r'logout', LogoutViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]