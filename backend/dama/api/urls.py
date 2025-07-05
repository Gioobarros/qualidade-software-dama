from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from api.view.ong import OngView
from api.view.publicacao import PublicacaoView
from api.view.usuario import UsuarioView
from api.view.auth import LoginView, LogoutView
from rest_framework.routers import DefaultRouter
from api.view.administrador import AdministradorView
from api.view.profissional import ProfissionalView

router = DefaultRouter()
router.register(r'publicacao', PublicacaoView, basename='publicacao')
router.register(r'ong', OngView, basename='ong')
router.register(r'profissional', ProfissionalView, basename='profissional')
router.register(r'admin', AdministradorView, basename='admin')
router.register(r'usuario', UsuarioView, basename='usuario')


# http://127.0.0.1:8000/api/publicacao/?data_inicio=(yyyy-mm-dd)&data_fim=(yyyy-mm-dd)&palavra_chave=&status

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
] 
urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)