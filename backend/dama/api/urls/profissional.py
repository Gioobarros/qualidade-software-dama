from rest_framework.routers import DefaultRouter
from api.view.profissional import ProfissionalViewSet

profissional_router = DefaultRouter()
profissional_router.register("profissional", ProfissionalViewSet, basename="profissional")