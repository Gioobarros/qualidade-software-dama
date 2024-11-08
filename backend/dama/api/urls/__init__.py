from django.urls import include, path 
from .administrador import admin_router 
from .ong import ong_router
from .profissional import profissional_router 
from .relato import relato_router
from .user import user_router

urlpatterns = [
    path('', include(admin_router.urls)),
    path('', include(ong_router.urls)),
    path('', include(profissional_router.urls)),
    path('', include(relato_router.urls)),
    path('', include(user_router.urls)),
]

