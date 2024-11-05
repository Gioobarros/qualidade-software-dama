from rest_framework.routers import DefaultRouter
from api.views.profissional import ProfissionalViewSet

profissional_router = DefaultRouter()
profissional_router.register("profissional", ProfissionalViewSet, basename="profissional")