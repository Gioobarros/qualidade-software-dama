from rest_framework.routers import DefaultRouter
from api.view.ong import OngViewSet

ong_router = DefaultRouter()
ong_router.register("ong", OngViewSet, basename="ong")