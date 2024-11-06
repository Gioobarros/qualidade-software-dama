from rest_framework.routers import DefaultRouter
from api.view.administrador import AdministradorViewSet

admin_router = DefaultRouter()
admin_router.register("admin", AdministradorViewSet, basename="admin")