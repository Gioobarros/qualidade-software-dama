from rest_framework.routers import DefaultRouter
from api.view.user import UserViewSet

user_router = DefaultRouter()
user_router.register("user", UserViewSet, basename="user")