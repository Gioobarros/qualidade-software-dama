from rest_framework.routers import DefaultRouter
from api.view.relato import RelatoViewSet

relato_router = DefaultRouter()
relato_router.register("relato", RelatoViewSet, basename="relato")