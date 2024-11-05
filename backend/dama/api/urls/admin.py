from rest_framework.routers import DefaultRouter
from api.views.admin import AdminViewSet

admin_router = DefaultRouter()
admin_router.register("admin", AdminViewSet, basename="admin")