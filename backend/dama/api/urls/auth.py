from rest_framework.routers import DefaultRouter
from api.view.auth import LoginViewSet, LogoutViewSet

auth_router = DefaultRouter()
auth_router.register("login", LoginViewSet, basename="login")
auth_router.register("logout", LogoutViewSet, basename="logout")