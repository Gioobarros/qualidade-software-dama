from . import views
from django.urls import path

app_name = 'dama'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('cadastro/', views.CadastroView.as_view(), name='cadastro'),
    path('relato/', views.RelatoView.as_view(), name='relato'),
]