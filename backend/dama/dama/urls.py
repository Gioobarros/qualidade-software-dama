from django.contrib import admin
from api.view.ong import OngViewSet
from django.urls import path, include
from api.view.relato import RelatoViewSet
from rest_framework.routers import DefaultRouter
from api.view.profissional import ProfissionalViewSet
from api.view.administrador import AdministradorViewSet 

router = DefaultRouter()
router.register(r'profissional', ProfissionalViewSet)
router.register(r'ong', OngViewSet)
router.register(r'relato', RelatoViewSet)
router.register(r'administrador', AdministradorViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
